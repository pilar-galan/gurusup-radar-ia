import math, random
W,H = 1200,630
DARK="#021f12"; MINT="#2ECF8F"
GOLD=math.radians(137.507)

def page(svg):
    return (f"<style>*{{margin:0;padding:0}}html,body{{width:{W}px;height:{H}px;"
            f"overflow:hidden;background:#ff00ff}}svg{{display:block}}</style>{svg}")

DEFS=f"""<defs>
 <radialGradient id="core" cx="34%" cy="28%" r="80%">
   <stop offset="0" stop-color="#6ae7b0"/><stop offset="52%" stop-color="{MINT}"/>
   <stop offset="100%" stop-color="#1a9d6c"/></radialGradient>
 <radialGradient id="coreD" cx="34%" cy="28%" r="80%">
   <stop offset="0" stop-color="#0a3b25"/><stop offset="60%" stop-color="{DARK}"/>
   <stop offset="100%" stop-color="#01150c"/></radialGradient>
 <filter id="big" x="-90%" y="-90%" width="280%" height="280%"><feGaussianBlur stdDeviation="34"/></filter>
 <filter id="mid" x="-90%" y="-90%" width="280%" height="280%"><feGaussianBlur stdDeviation="12"/></filter>
 <filter id="far" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>
</defs>"""

def core(cx,cy,r,light=True):
    g=MINT if light else DARK
    o=[f'<g filter="url(#mid)"><circle cx="{cx}" cy="{cy}" r="{r+7}" fill="{g}" opacity="{.55 if light else .35}"/></g>']
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{"core" if light else "coreD"})"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{"#ffffff" if light else DARK}" stroke-opacity="{.42 if light else .5}" stroke-width="1.2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r-13}" fill="none" stroke="{"#ffffff" if light else MINT}" stroke-opacity="{.16 if light else .22}" stroke-width="1"/>')
    return "".join(o)

def hexgrid(step=46, jitter=0.0, seed=1):
    rnd=random.Random(seed); pts=[]
    rows=int(H/(step*0.866))+3
    for j in range(-1,rows):
        y=j*step*0.866
        off=(step/2) if j%2 else 0
        for i in range(-1,int(W/step)+2):
            x=i*step+off
            if jitter: x+=rnd.uniform(-jitter,jitter); y2=y+rnd.uniform(-jitter,jitter)
            else: y2=y
            pts.append((x,y2))
    return pts

# ---------- 1 · constelación de agentes ----------
def constelacion():
    cx,cy=600,315
    s=[f'<rect width="{W}" height="{H}" fill="{DARK}"/>',
       f'<g filter="url(#big)"><ellipse cx="{cx}" cy="{cy}" rx="340" ry="250" fill="{MINT}" opacity=".24"/></g>',
       f'<g filter="url(#big)"><ellipse cx="1140" cy="60" rx="200" ry="150" fill="{MINT}" opacity=".08"/></g>']
    pts=[p for p in hexgrid(58, 9, 4) if math.dist(p,(cx,cy))>150]
    # links between close neighbours (structured mesh)
    for i,p in enumerate(pts):
        for q in pts[i+1:]:
            d=math.dist(p,q)
            if d<64:
                dm=(math.dist(p,(cx,cy))+math.dist(q,(cx,cy)))/2
                op=max(.035,.32-dm/1250)
                s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{MINT}" stroke-opacity="{op:.3f}" stroke-width=".9"/>')
    for p in pts:
        d=math.dist(p,(cx,cy)); r=max(1.6,5.4-d/190)
        op=max(.14,.9-d/560); f=' filter="url(#far)"' if d>360 else ''
        s.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r:.1f}" fill="{MINT}" fill-opacity="{op:.2f}"{f}/>')
    # agentes satélite repartidos por ángulo
    sats=[]
    for k in range(7):
        a=-math.pi/2+k*GOLD
        rr=208+((k*53)%92)
        sats.append((cx+rr*math.cos(a), cy+rr*0.74*math.sin(a)))
    for (x,y) in sats:
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{MINT}" stroke-opacity=".42" stroke-width="1.2"/>')
    for (x,y) in sats:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="#04321e" stroke="{MINT}" stroke-opacity=".8" stroke-width="1.4"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.4" fill="{MINT}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="122" fill="none" stroke="{MINT}" stroke-opacity=".22" stroke-width="1"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="122" fill="none" stroke="{MINT}" stroke-opacity=".6" stroke-width="1.3" stroke-dasharray="2 15" stroke-linecap="round"/>')
    s.append(core(cx,cy,60))
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{"".join(s)}</svg>'

# ---------- 2 · flujo que atraviesa el núcleo ----------
def flujo():
    cx,cy,R=600,315,64
    s=[f'<rect width="{W}" height="{H}" fill="{DARK}"/>',
       f'<g filter="url(#big)"><ellipse cx="{cx}" cy="{cy}" rx="380" ry="210" fill="{MINT}" opacity=".20"/></g>']
    N=34
    for i in range(N):
        t=i/(N-1); y0=10+t*(H-20)
        edge=(1-abs(t-.5)*2)
        op=.10+.42*edge**1.5; w=.85+1.35*edge**2
        s.append(f'<path d="M-40 {y0:.1f} C {cx-360} {y0:.1f}, {cx-140} {cy}, {cx} {cy}" fill="none" '
                 f'stroke="{MINT}" stroke-opacity="{op:.3f}" stroke-width="{w:.2f}" stroke-linecap="round"/>')
        s.append(f'<path d="M{cx} {cy} C {cx+140} {cy}, {cx+360} {y0:.1f}, {W+40} {y0:.1f}" fill="none" '
                 f'stroke="{MINT}" stroke-opacity="{op*.82:.3f}" stroke-width="{w:.2f}" stroke-linecap="round"/>')
        if i%4==1:
            s.append(f'<circle cx="{170+ (i%3)*40}" cy="{y0:.1f}" r="2.4" fill="{MINT}" fill-opacity=".45"/>')
            s.append(f'<circle cx="{W-170-(i%3)*40}" cy="{y0:.1f}" r="2.4" fill="{MINT}" fill-opacity=".38"/>')
    for r,o,dash in ((R+52,.26,None),(R+96,.13,None),(R+72,.55,"2 16")):
        da=f' stroke-dasharray="{dash}" stroke-linecap="round"' if dash else ''
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MINT}" stroke-opacity="{o}" stroke-width="1.15"{da}/>')
    s.append(core(cx,cy,R))
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{"".join(s)}</svg>'

# ---------- 3 · malla discreta (sutil) ----------
def malla():
    cx,cy=600,300
    s=[f'<rect width="{W}" height="{H}" fill="{DARK}"/>',
       f'<g filter="url(#big)"><ellipse cx="{cx}" cy="{cy}" rx="430" ry="260" fill="{MINT}" opacity=".16"/></g>',
       f'<g filter="url(#big)"><ellipse cx="140" cy="600" rx="240" ry="160" fill="{MINT}" opacity=".07"/></g>']
    for p in hexgrid(38,0,2):
        d=math.dist(p,(cx,cy))
        k=max(0.0,1-d/560)
        r=1.1+2.3*k**1.7
        op=.10+.55*k**1.6
        s.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r:.2f}" fill="{MINT}" fill-opacity="{op:.3f}"/>')
    for k,(r,o) in enumerate(((118,.30),(196,.20),(286,.13),(388,.08))):
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MINT}" stroke-opacity="{o}" stroke-width="1"/>')
        if k<2:
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MINT}" stroke-opacity="{o*2.1:.2f}" stroke-width="1.2" stroke-dasharray="2 17" stroke-linecap="round"/>')
    for k in range(5):
        a=-math.pi/3+k*GOLD; rr=(118,196,196,286,388)[k]
        x,y=cx+rr*math.cos(a), cy+rr*math.sin(a)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{9-k:.0f}" fill="{MINT}" fill-opacity="{.85-k*.13:.2f}"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{18-k:.0f}" fill="none" stroke="{MINT}" stroke-opacity="{.5-k*.08:.2f}" stroke-width="1.1"/>')
    s.append(f'<g filter="url(#mid)"><circle cx="{cx}" cy="{cy}" r="30" fill="{MINT}" opacity=".85"/></g>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{MINT}"/>')
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{"".join(s)}</svg>'

# ---------- 4 · versión menta ----------
def menta():
    cx,cy=600,315
    s=[f'<rect width="{W}" height="{H}" fill="{MINT}"/>',
       f'<g filter="url(#big)"><ellipse cx="{cx}" cy="{cy}" rx="440" ry="300" fill="#79eeba" opacity=".7"/></g>']
    pts=[p for p in hexgrid(66,10,6) if math.dist(p,(cx,cy))>150]
    for i,p in enumerate(pts):
        for q in pts[i+1:]:
            if math.dist(p,q)<72:
                dm=(math.dist(p,(cx,cy))+math.dist(q,(cx,cy)))/2
                s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{DARK}" stroke-opacity="{max(.04,.16-dm/3000):.3f}" stroke-width=".9"/>')
    for p in pts:
        d=math.dist(p,(cx,cy))
        s.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{max(1.6,4.6-d/230):.1f}" fill="{DARK}" fill-opacity="{max(.13,.5-d/1000):.2f}"/>')
    sats=[]
    for k in range(6):
        a=-math.pi/2+k*GOLD; rr=205+((k*61)%80)
        sats.append((cx+rr*math.cos(a), cy+rr*0.76*math.sin(a)))
    for (x,y) in sats:
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{DARK}" stroke-opacity=".34" stroke-width="1.15"/>')
    for (x,y) in sats:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="18" fill="none" stroke="{DARK}" stroke-opacity=".38" stroke-width="1.2"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8.5" fill="{DARK}" fill-opacity=".9"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="116" fill="none" stroke="{DARK}" stroke-opacity=".2" stroke-width="1"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="116" fill="none" stroke="{DARK}" stroke-opacity=".45" stroke-width="1.2" stroke-dasharray="2 15" stroke-linecap="round"/>')
    s.append(core(cx,cy,62,light=False))
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}{"".join(s)}</svg>'

for n,f in (("v1",constelacion),("v2",flujo),("v3",malla),("v4",menta)):
    open(f"{n}.html","w").write(page(f())); print("ok",n)
