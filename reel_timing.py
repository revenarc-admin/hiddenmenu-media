import content_v3 as c, content_gift as g
P = dict(c.P); P.update(g.P)
def _w(o):
    if isinstance(o, str): return len(o.split())
    if isinstance(o, dict): return sum(_w(v) for k, v in o.items() if k not in ("kind", "type"))
    if isinstance(o, (list, tuple)): return sum(_w(v) for v in o)
    return 0
def durations(day, n):
    s = [x for x in P[day][1] if x.get("label") != "To be fair"]
    out = []
    for i, x in enumerate(s[:n]):
        t = 3.5 if i == 0 else max(3.0, 1.5 + _w(x) / 3.0)
        out.append(round(min(t, 10.0), 1))
    while len(out) < n: out.append(5.0)
    return out
