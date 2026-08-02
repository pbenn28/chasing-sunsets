document.addEventListener('DOMContentLoaded', function () {
    const list = document.getElementById('bill-list');
    if (!list) return;

    const cards = Array.from(list.querySelectorAll('.bill-card'));
    const searchInput = document.getElementById('search-input');
    const topicFilter = document.getElementById('filter-topic');
    const statusFilter = document.getElementById('filter-status');
    const chamberFilter = document.getElementById('filter-chamber');
    const sortSelect = document.getElementById('sort-select');
    const resultsCount = document.getElementById('results-count');
    const noResults = document.getElementById('no-results');

    // ---- Scoring: weights + live recompute ----
    const weightSliders = Array.from(document.querySelectorAll('.weight-slider'));
    const weightsReset = document.getElementById('weights-reset');

    const DEFAULT_WEIGHTS = {};
    weightSliders.forEach(function (slider) {
        DEFAULT_WEIGHTS['w_' + slider.dataset.weight] = parseFloat(slider.value);
    });
    let currentWeights = Object.assign({}, DEFAULT_WEIGHTS);

    function computeS(axes, weights) {
        const raw = weights.w_A * axes.A + weights.w_B * axes.B + weights.w_C * axes.C + weights.w_D * axes.D + weights.w_F * axes.F;
        return Math.max(-5, Math.min(5, raw));
    }

    function computeImpact(components) {
        const { R, D, E_f, P } = components;
        return 10 * (0.35 * R + 0.30 * D + 0.20 * E_f + 0.15 * P);
    }

    function computeExpectedImpact(impact, pEnact) {
        return impact * (pEnact || 0);
    }

    function readCardScoring(card) {
        const blob = card.querySelector('.bill-scoring-data');
        if (!blob) return null;
        try { return JSON.parse(blob.textContent); } catch (e) { return null; }
    }

    const cardScoring = new Map();
    cards.forEach(function (c) { cardScoring.set(c, readCardScoring(c)); });

    function renderDots(el, filledCount, max) {
        if (!el) return;
        el.innerHTML = '';
        for (let i = 1; i <= max; i++) {
            const dot = document.createElement('span');
            let cls = 'dot';
            if (i <= filledCount) cls += ' filled';
            else if ((i - 0.5) <= filledCount) cls += ' half';
            dot.className = cls;
            el.appendChild(dot);
        }
    }

    function recomputeCard(card) {
        const data = cardScoring.get(card);
        if (!data) return; // unscored bill -- leave server-rendered zero defaults in place

        const s = computeS(data.axes, currentWeights);
        const impact = computeImpact(data.impact_components);
        const pEnact = data.likelihood.p_enact || 0;
        const expectedImpact = computeExpectedImpact(impact, pEnact);

        card.dataset.s = s.toFixed(2);
        card.dataset.impact = impact.toFixed(2);
        card.dataset.pEnact = pEnact.toFixed(3);
        card.dataset.expectedImpact = expectedImpact.toFixed(3);

        const sMarker = card.querySelector('.s-marker');
        if (sMarker) sMarker.style.left = (((s + 5) / 10) * 100).toFixed(1) + '%';
        const sValue = card.querySelector('.s-value');
        if (sValue) sValue.textContent = (s >= 0 ? '+' : '') + s.toFixed(1);
        const pEnactValue = card.querySelector('.p-enact-value');
        if (pEnactValue) pEnactValue.textContent = Math.round(pEnact * 100) + '%';
        renderDots(card.querySelector('.impact-dots'), impact / 2, 5);
    }

    function recomputeAll() {
        cards.forEach(recomputeCard);
        applyFilters();
        applySort();
    }

    // ---- Chart geometry ----
    const NS = 'http://www.w3.org/2000/svg';
    const svg = document.getElementById('chart-svg');
    const readout = document.getElementById('chart-readout');
    const tooltip = document.getElementById('chart-tooltip');

    // Tapping the chart background (not a point) dismisses an open tooltip
    // instead of leaving it stuck open with no way to clear it on touch.
    svg.addEventListener('pointerup', function (e) {
        if (e.target === svg || e.target.tagName !== 'circle') {
            tooltip.hidden = true;
            activeTouchPt = null;
        }
    });

    function positionTooltip(e) {
        const off = 14;
        let x = e.clientX + off, y = e.clientY + off;
        const tw = tooltip.offsetWidth, th = tooltip.offsetHeight;
        if (x + tw > window.innerWidth - 8) x = e.clientX - off - tw;
        if (y + th > window.innerHeight - 8) y = e.clientY - off - th;
        tooltip.style.left = x + 'px';
        tooltip.style.top = y + 'px';
    }
    const VB_W = 720, VB_H = 460;
    const padL = 70, padR = 24, padT = 24, padB = 56;
    const plotW = VB_W - padL - padR;
    const plotH = VB_H - padT - padB;
    const S_MIN = -5, S_MAX = 5, PE_MIN = 0, PE_MAX = 1;

    const xOf = s => padL + ((s - S_MIN) / (S_MAX - S_MIN)) * plotW;
    const yOf = pe => padT + ((PE_MAX - pe) / (PE_MAX - PE_MIN)) * plotH;

    function lerp(a, b, t) { return a + (b - a) * t; }
    function safetyColor(s) {
        // Positive S (safety/restriction) -> royalblue. Negative S (deregulation/accel) -> orange.
        // White sits exactly at S = 0.
        const t = (s - S_MIN) / (S_MAX - S_MIN); // 0..1, 0.5 = neutral
        const stops = [
            [0.0, [237, 162, 87]],
            [0.5, [255, 255, 255]],
            [1.0, [65, 105, 225]]
        ];
        let lo = stops[0], hi = stops[stops.length - 1];
        for (let i = 0; i < stops.length - 1; i++) {
            if (t >= stops[i][0] && t <= stops[i + 1][0]) { lo = stops[i]; hi = stops[i + 1]; break; }
        }
        const seg = (t - lo[0]) / (hi[0] - lo[0] || 1);
        const c = [0, 1, 2].map(k => Math.round(lerp(lo[1][k], hi[1][k], seg)));
        return `rgb(${c[0]}, ${c[1]}, ${c[2]})`;
    }

    function el(tag, attrs) {
        const n = document.createElementNS(NS, tag);
        for (const k in attrs) n.setAttribute(k, attrs[k]);
        return n;
    }

    let activeTouchPt = null;

    function drawChart(visible) {
        activeTouchPt = null;
        if (tooltip) tooltip.hidden = true;
        while (svg.firstChild) svg.removeChild(svg.firstChild);

        // gridlines + Y ticks (P(enact) 0..1, shown as %)
        [0, 0.25, 0.5, 0.75, 1.0].forEach(pe => {
            const y = yOf(pe);
            svg.appendChild(el('line', { class: 'grid-line', x1: padL, y1: y, x2: padL + plotW, y2: y }));
            const t = el('text', { class: 'axis-text', x: padL - 10, y: y + 4, 'text-anchor': 'end' });
            t.textContent = Math.round(pe * 100) + '%';
            svg.appendChild(t);
        });
        // X ticks (S -5..+5)
        [-5, -2.5, 0, 2.5, 5].forEach(s => {
            const x = xOf(s);
            const t = el('text', { class: 'axis-text', x: x, y: padT + plotH + 20, 'text-anchor': 'middle' });
            t.textContent = s > 0 ? '+' + s : s;
            svg.appendChild(t);
        });
        // axes
        svg.appendChild(el('line', { class: 'axis-line', x1: padL, y1: padT + plotH, x2: padL + plotW, y2: padT + plotH }));
        svg.appendChild(el('line', { class: 'axis-line', x1: padL, y1: padT, x2: padL, y2: padT + plotH }));
        // neutral zero line
        svg.appendChild(el('line', { class: 'zero-line', x1: xOf(0), y1: padT, x2: xOf(0), y2: padT + plotH }));

        // axis titles + poles
        const xt = el('text', { class: 'axis-title', x: padL + plotW / 2, y: VB_H - 8, 'text-anchor': 'middle' });
        xt.textContent = 'Deregulation / accel.  ⟵ ⟶  Safety / restriction';
        svg.appendChild(xt);
        const yt = el('text', { class: 'axis-title', x: 18, y: padT + plotH / 2, 'text-anchor': 'middle', transform: `rotate(-90 18 ${padT + plotH / 2})` });
        yt.textContent = 'Probability of enactment  ⟶';
        svg.appendChild(yt);

        if (!visible.length) {
            readout.innerHTML = 'No bills match the current filters.';
            return;
        }

        // Bills scored from a summary rather than the bill's actual full text
        // (data-in-scatter="false") are dropped from the chart entirely, not
        // just shown unfilled -- see "How the probability model works" above.
        const plottable = visible.filter(c => c.dataset.scored !== 'true' || c.dataset.inScatter === 'true');
        const pendingCount = visible.length - plottable.length;
        const scoredVisible = plottable.filter(c => c.dataset.scored === 'true');

        // enactment-probability-weighted center of gravity of S (scored bills only)
        let wnum = 0, wden = 0, plainSum = 0;
        scoredVisible.forEach(c => {
            const s = parseFloat(c.dataset.s), pe = parseFloat(c.dataset.pEnact);
            wnum += s * pe; wden += pe; plainSum += s;
        });
        const wmean = wden ? wnum / wden : 0;
        const plainMean = scoredVisible.length ? plainSum / scoredVisible.length : 0;
        const pendingNote = pendingCount
            ? ` (${pendingCount} more bill${pendingCount === 1 ? '' : 's'} shown below ${pendingCount === 1 ? 'is' : 'are'} pending full-text verification and not plotted here.)`
            : '';

        if (!plottable.length) {
            readout.innerHTML = `None of the ${visible.length} bill${visible.length === 1 ? '' : 's'} shown ${visible.length === 1 ? 'is' : 'are'} eligible for the chart yet` + (pendingCount ? ' — all are pending full-text verification.' : '.');
            return;
        }

        // points (grouped by exact coordinate so ties fan out evenly and never overlap)
        const coordGroups = new Map();
        plottable.forEach((c, i) => {
            const key = c.dataset.s + '|' + c.dataset.pEnact;
            if (!coordGroups.has(key)) coordGroups.set(key, []);
            coordGroups.get(key).push(i);
        });
        plottable.forEach((c, i) => {
            const s = parseFloat(c.dataset.s);
            const pe = parseFloat(c.dataset.pEnact);
            const im = parseFloat(c.dataset.impact);
            const scored = c.dataset.scored === 'true';
            const group = coordGroups.get(c.dataset.s + '|' + c.dataset.pEnact);
            const n = group.length;
            let jx = 0, jy = 0;
            if (n > 1) {
                const k = group.indexOf(i);
                const angle = (2 * Math.PI * k) / n;
                const radius = 3 + Math.min(n, 8) * 0.6;
                jx = Math.cos(angle) * radius;
                jy = Math.sin(angle) * radius;
            }
            const r = 1.5 + im * 1.1;
            const name = ((c.querySelector('.bill-title') || {}).textContent || c.id).trim() + (scored ? '' : ' (not yet scored)');
            const ptAttrs = {
                class: 'pt', cx: xOf(s) + jx, cy: yOf(pe) + jy, r: r,
                'data-slug': c.id, 'aria-label': name
            };
            if (scored) {
                ptAttrs.fill = safetyColor(s);
            } else {
                ptAttrs.fill = '#e5e5e5';
                ptAttrs.stroke = '#999';
                ptAttrs['stroke-width'] = 1;
            }
            const pt = el('circle', ptAttrs);
            pt.addEventListener('mouseenter', function (e) {
                tooltip.textContent = name;
                tooltip.hidden = false;
                positionTooltip(e);
            });
            pt.addEventListener('mousemove', positionTooltip);
            pt.addEventListener('mouseleave', function () { tooltip.hidden = true; });
            pt.addEventListener('pointerup', function (e) {
                // On touch, the first tap on a point only reveals its name --
                // it takes a second tap on the same point to open the bill.
                // Otherwise a tap you meant as "what is that?" immediately
                // navigates you away before you can read the tooltip.
                if (e.pointerType === 'touch' && activeTouchPt !== pt) {
                    tooltip.textContent = name;
                    tooltip.hidden = false;
                    positionTooltip(e);
                    activeTouchPt = pt;
                    e.preventDefault();
                    return;
                }
                tooltip.hidden = true;
                activeTouchPt = null;
                const card = document.getElementById(c.id);
                if (card) { card.open = true; card.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
            });
            svg.appendChild(pt);
        });

        if (!scoredVisible.length) {
            readout.innerHTML = `None of the ${plottable.length} bill${plottable.length === 1 ? '' : 's'} plotted ${plottable.length === 1 ? 'has' : 'have'} been scored yet.` + pendingNote;
            return;
        }

        // weighted-mean line
        const wx = xOf(wmean);
        svg.appendChild(el('line', { class: 'wmean-line', x1: wx, y1: padT - 6, x2: wx, y2: padT + plotH }));
        const wl = el('text', { class: 'wmean-label', x: wx, y: padT - 12, 'text-anchor': (wmean > 2 ? 'end' : 'middle') });
        wl.textContent = 'weighted avg ' + (wmean >= 0 ? '+' : '') + wmean.toFixed(1);
        svg.appendChild(wl);

        let lean;
        if (wmean <= -0.5) lean = 'leans <strong>deregulation/acceleration</strong>';
        else if (wmean >= 0.5) lean = 'leans <strong>safety/restriction</strong>';
        else lean = 'sits <strong>near neutral</strong>';
        readout.innerHTML =
            `Across the ${scoredVisible.length} scored bill${scoredVisible.length === 1 ? '' : 's'} shown, the enactment-probability-weighted center of gravity is ` +
            `<strong>${wmean >= 0 ? '+' : ''}${wmean.toFixed(1)}</strong> on the −5 (deregulation) to +5 (safety/restriction) scale — the active agenda ${lean}. ` +
            `(Unweighted, counting every scored bill equally: ${plainMean >= 0 ? '+' : ''}${plainMean.toFixed(1)}.)` + pendingNote;
    }

    function applyFilters() {
        const term = searchInput.value.trim().toLowerCase();
        const topic = topicFilter.value;
        const status = statusFilter.value;
        const chamber = chamberFilter.value;
        let visible = [];

        cards.forEach(function (card) {
            const matchesSearch = !term || card.dataset.search.includes(term);
            const matchesTopic = topic === 'all' || card.dataset.topic === topic;
            const matchesStatus = status === 'all' || card.dataset.status === status;
            const matchesChamber = chamber === 'all' || card.dataset.chamber === chamber;
            const vis = matchesSearch && matchesTopic && matchesStatus && matchesChamber;
            card.hidden = !vis;
            if (vis) visible.push(card);
        });

        resultsCount.textContent = 'Showing ' + visible.length + ' of ' + cards.length + ' bills';
        noResults.hidden = visible.length !== 0;
        drawChart(visible);
    }

    function applySort() {
        const mode = sortSelect.value;
        const sorted = cards.slice().sort(function (a, b) {
            switch (mode) {
                case 'impact-desc':
                    return Number(b.dataset.impact) - Number(a.dataset.impact);
                case 's-asc':
                    return Number(b.dataset.s) - Number(a.dataset.s);
                case 's-desc':
                    return Number(a.dataset.s) - Number(b.dataset.s);
                case 'p-enact-desc':
                    return Number(b.dataset.pEnact) - Number(a.dataset.pEnact);
                case 'date-desc':
                    return (b.dataset.date || '').localeCompare(a.dataset.date || '');
                case 'topic': {
                    const t = (a.dataset.topic || '').localeCompare(b.dataset.topic || '');
                    if (t !== 0) return t;
                    return Number(b.dataset.pEnact) - Number(a.dataset.pEnact);
                }
                case 'alpha':
                    return a.querySelector('.bill-title').textContent
                        .localeCompare(b.querySelector('.bill-title').textContent);
                case 'expected-impact-desc':
                default:
                    return Number(b.dataset.expectedImpact) - Number(a.dataset.expectedImpact);
            }
        });
        sorted.forEach(function (card) { list.appendChild(card); });
    }

    function openFromHash() {
        if (!location.hash) return;
        const target = document.getElementById(location.hash.slice(1));
        if (target && target.classList.contains('bill-card')) {
            target.open = true;
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    searchInput.addEventListener('input', applyFilters);
    topicFilter.addEventListener('change', applyFilters);
    statusFilter.addEventListener('change', applyFilters);
    chamberFilter.addEventListener('change', applyFilters);
    sortSelect.addEventListener('change', applySort);

    weightSliders.forEach(function (slider) {
        const key = 'w_' + slider.dataset.weight;
        const valueEl = document.getElementById('w' + slider.dataset.weight.toLowerCase() + '-value');
        slider.addEventListener('input', function () {
            currentWeights[key] = parseFloat(this.value);
            if (valueEl) valueEl.textContent = parseFloat(this.value).toFixed(2);
            recomputeAll();
        });
    });
    if (weightsReset) {
        weightsReset.addEventListener('click', function () {
            currentWeights = Object.assign({}, DEFAULT_WEIGHTS);
            weightSliders.forEach(function (slider) {
                const key = 'w_' + slider.dataset.weight;
                const valueEl = document.getElementById('w' + slider.dataset.weight.toLowerCase() + '-value');
                slider.value = DEFAULT_WEIGHTS[key];
                if (valueEl) valueEl.textContent = DEFAULT_WEIGHTS[key].toFixed(2);
            });
            recomputeAll();
        });
    }

    recomputeAll();
    openFromHash();
});
