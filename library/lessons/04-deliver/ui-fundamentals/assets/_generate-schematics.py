import os,sys
R=sys.argv[1]
INK,GH,MU,AC,BG="#1a1a1a","#c9c9c9","#8a8a8a","#6B46C1","#ffffff"
def svg(w,h,body,name,sub):
    p=os.path.join(R,sub);os.makedirs(p,exist_ok=True)
    open(os.path.join(p,name),"w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="JetBrains Mono, monospace" font-size="16"><rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')
def bar(x,y,w,h=8,c=GH):
    sw=max(2,round(h/3)); return f'<line x1="{x+sw/2}" y1="{y+h/2}" x2="{x+w-sw/2}" y2="{y+h/2}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round"/>'
def frame(x,y,w,h,s=INK,sw=1.5,d=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{s}" stroke-width="{sw}" {d}/>'
def t(x,y,s,c=INK,a="start",sz=16): return f'<text x="{x}" y="{y}" fill="{c}" text-anchor="{a}" font-size="{sz}">{s}</text>'
def brk(x,y1,y2,lab): # vertical measurement bracket
    return f'<path d="M{x} {y1}v{y2-y1}M{x-6} {y1}h12M{x-6} {y2}h12" stroke="{AC}" stroke-width="2" fill="none"/>'+t(x+12,(y1+y2)/2+5,lab,AC)
def card(x,y,w,h,heading=70,lines=(180,150,170)):
    b=bar(x,y,heading,12,MU)
    for i,l in enumerate(lines): b+=bar(x,y+28+i*16,l)
    return b
# 1 proximity: same 6 items, two spacings
def prox():
    b=t(40,40,"gap 24px  /  gap 8px"," ",)[:0]
    b=""
    for i,(ox,g) in enumerate([(60,24),(500,8)]):
        b+=frame(ox-30,50,360,280)
        y=90
        for k in range(6):
            b+=bar(ox,y,200 if k%2==0 else 140,10,MU if k in(0,3) else GH);y+=20+ (g if k%2 else 0)+ (0)
        b+=t(ox-30,360,("heading 8 / group 24","heading 8 / group 8")[i],MU)
    return b
# keep it simple: explicit
def proximity():
    b=""
    for ox,gap,lab in [(60,"24","24px between groups"),(500,"8","8px between groups")]:
        g=int(gap);b+=frame(ox-30,40,360,300)
        y=80
        for grp in range(2):
            b+=bar(ox,y,110,12,MU);b+=bar(ox,y+20,220);b+=bar(ox,y+36,190);y+=36+8+g
            if grp==0: b+=brk(ox+250,y-g,y,gap) if True else ""
        b+=t(ox-30,375,lab,MU)
    svg(880,400,b,"proximity-24-vs-8.svg","layer-1-space")
def region():
    b=""
    # left: items close but across card edge; right: items far but same card
    b+=frame(30,40,380,260)+frame(60,70,150,200,MU,1)+frame(230,70,150,200,MU,1)
    b+=card(75,90,90,(110,90,100))+card(245,90,90,(110,90,100))
    b+=bar(75,230,90,28,MU)+bar(245,230,90,28,MU)
    b+=t(30,335,"card per group",MU)
    b+=frame(470,40,380,260)+frame(500,70,320,200,MU,1)
    b+=card(515,90,90,(110,90,100))+card(695,90,90,(110,90,100))
    b+=bar(515,230,90,28,MU)+bar(695,230,90,28,MU)
    b+=t(470,335,"one card, same gap",MU)
    svg(880,360,b,"common-region-two-boundaries.svg","layer-1-space")
def grid8():
    b=""
    for gx in range(0,81):
        pass
    for i in range(0,360,8): b+=f'<path d="M40 {40+i}H440" stroke="#e6e6e6"/>'
    for i in range(0,400,8): b+=f'<path d="M{40+i} 40V400" stroke="#e6e6e6"/>'
    ys=[56,104,128,200]
    for y,w in zip(ys,(180,260,220,140)): b+=bar(56,y,w,16 if y==56 else 10,MU if y==56 else GH)
    b+=brk(480,56,104,"48")+brk(480,104,128,"24")+brk(480,128,200,"72")
    b+=t(40,430,"every gap is a multiple of 8",MU)
    svg(640,450,b,"8pt-grid-overlay.svg","layer-1-space")
def twofirsts():
    b=""
    for ox,lab,two in [(40,"two firsts",True),(480,"one first",False)]:
        b+=frame(ox,40,380,300)+bar(ox+30,80,160,26,MU)
        b+=bar(ox+30,130,260,10)+bar(ox+30,150,220,10)
        b+=f'<rect x="{ox+30}" y="200" width="150" height="44" rx="8" fill="{INK}"/>'
        b+=f'<rect x="{ox+200}" y="200" width="150" height="44" rx="8" fill="{INK if two else "none"}" stroke="{INK if two else MU}" stroke-width="2"/>'
        b+=t(ox,375,lab,MU)
    svg(880,400,b,"two-firsts-vs-one-first.svg","layer-2-hierarchy")
def levers():
    b=""
    items=[("size",lambda x:bar(x,100,120,36,MU)+bar(x,150,120,8)),("weight",lambda x:bar(x,110,120,14,INK)+bar(x,140,120,5)),("colour",lambda x:bar(x,110,120,14,AC)+bar(x,140,120,14)),("space",lambda x:bar(x,100,120,14,MU)+bar(x,170,120,14))]
    for i,(l,f) in enumerate(items):
        x=40+i*220;b+=frame(x-20,60,180,160)+f(x)+t(x-20,255,l,MU)
    svg(900,290,b,"four-levers.svg","layer-2-hierarchy")
def fpattern():
    b=frame(40,40,420,320)+bar(60,70,380,18,MU)+bar(60,100,340,10)
    b+=bar(60,150,380,14,MU)+bar(60,170,300,8)+bar(60,184,260,8)
    for y in range(220,330,18): b+=bar(60,y,120,8)
    b+=f'<path d="M60 79H440M60 157H400M60 79V330" stroke="{AC}" stroke-width="3" fill="none" stroke-linecap="round" stroke-dasharray="2 8" opacity=".9"/>'
    b+=t(40,395,"scan path: top bar, second bar, down the left edge",MU)
    svg(500,420,b,"f-pattern-scan-path.svg","layer-2-hierarchy")
def vonrestorff():
    b=""
    for ox,n,lab in [(40,1,"one emphasised"),(40,3,"three emphasised")]: pass
    for r,(n,lab) in enumerate([(1,"one emphasised: it is noticed"),(3,"three emphasised: none is noticed")]):
        y=60+r*150
        for i in range(6):
            em=(i==2) if n==1 else i in(0,2,4)
            b+=f'<rect x="{40+i*100}" y="{y}" width="80" height="50" rx="8" fill="{INK if em else "none"}" stroke="{INK if em else MU}" stroke-width="2"/>'
        b+=t(40,y+90,lab,MU)
    svg(680,330,b,"von-restorff-emphasis-budget.svg","layer-2-hierarchy")
def typescale():
    b=frame(40,40,420,300)
    b+=bar(70,80,220,28,INK)+t(480,100,"28 / 700",MU)
    b+=bar(70,140,300,16,MU)+t(480,154,"16 / 600",MU)
    for y in (180,200,220): b+=bar(70,y,340 if y<220 else 260,8)
    b+=t(480,206,"14 / 400",MU)
    b+=bar(70,270,120,6)+t(480,278,"12 / 400",MU)
    svg(640,370,b,"type-scale-three-sizes.svg","layer-3-type")
def roles():
    b=""
    for i,(l,c,f) in enumerate([("brand",AC,1),("neutral",MU,1),("success","#2f9e6b",1),("warning","#e0a000",1),("error","#d64545",1)]):
        x=40+i*150;b+=f'<rect x="{x}" y="60" width="120" height="80" rx="8" fill="none" stroke="{c}" stroke-width="3"/>'+t(x,170,l,MU)
    b+=t(40,230,"one colour = one job",MU)
    svg(800,260,b,"colour-roles.svg","layer-4-colour")
def tokenaudit():
    rows=[("spacing","4  8  12  16  20  24  30  32"),("type sizes","11 12 13 14 15 16 18 24"),("greys","#888  #8a8a8a  #999")]
    b=frame(40,40,640,40*len(rows)+60)+t(60,75,"token | values found | defined?",MU)
    for i,(a,v) in enumerate(rows): b+=t(60,115+i*40,a)+t(220,115+i*40,v,MU)+t(560,115+i*40,"?",AC)
    svg(720,260,b,"token-audit-template.svg","layer-4-colour")
def states():
    b=""
    sts=["default","hover","focus","active","disabled","loading","error","empty"]
    for i,s in enumerate(sts):
        x=40+(i%4)*210;y=50+(i//4)*130
        w,h=170,48
        if s=="default": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{INK}"/>'
        elif s=="hover": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{INK}" stroke-width="3"/>'
        elif s=="focus": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{INK}"/><rect x="{x-6}" y="{y-6}" width="{w+12}" height="{h+12}" rx="12" fill="none" stroke="{AC}" stroke-width="2"/>'
        elif s=="active": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{MU}"/>'
        elif s=="disabled": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{GH}" stroke-width="2" stroke-dasharray="4 4"/>'
        elif s=="loading": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="{x+w/2-16}" cy="{y+h/2}" r="3" fill="{INK}"/><circle cx="{x+w/2}" cy="{y+h/2}" r="3" fill="{INK}"/><circle cx="{x+w/2+16}" cy="{y+h/2}" r="3" fill="{INK}"/>'
        elif s=="error": r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{AC}" stroke-width="3"/>'
        else: r=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{MU}" stroke-width="2" stroke-dasharray="2 6"/>'
        b+=r+t(x,y+84,s,MU)
    svg(900,330,b,"button-states-checklist.svg","layer-5-components")
def tesler():
    b=frame(40,40,260,200)+t(60,70,"user",MU)+bar(60,95,100,40,AC)+t(40,275,"complexity here",MU)
    b+=frame(380,40,260,200)+t(400,70,"system",MU)+bar(400,95,100,40,AC)+t(380,275,"or here",MU)
    svg(700,300,b,"tesler-complexity-moves.svg","laws-of-ux")
def jakob():
    b=frame(40,40,300,120)+frame(40,40,300,0)+bar(60,70,120,10)+t(40,200,"familiar position",MU)
    b+=frame(400,40,300,120)+bar(500,70,120,10)+t(400,200,"moved: user relearns",MU)
    svg(740,230,b,"jakob-familiar-vs-moved.svg","laws-of-ux")
for f in (proximity,region,grid8,twofirsts,levers,fpattern,vonrestorff,typescale,roles,tokenaudit,states,tesler,jakob): f()

# ---- cheat sheet (mentee practice) ----
def cheatsheet():
    W,H=1500,1130
    S='font-family="Inter, Helvetica, Arial, sans-serif"'
    b=f'<text x="40" y="80" {S} font-size="54" font-weight="800" fill="{INK}">5 layer để đánh giá một màn hình</text>'
    b+=f'<text x="40" y="115" {S} font-size="20" fill="{MU}">Đọc theo thứ tự, dừng ở layer đầu tiên không ổn. Mỗi layer kết thúc bằng một câu nói được với developer.</text>'
    P=[("1. Space","Cái nào thuộc nhóm nào?",["Mọi khoảng cách là bội số của 8.","Cùng nhóm: gap nhỏ. Khác nhóm: gap lớn.","Đừng dùng border để sửa lỗi spacing."],"“Hai cái này cùng nhóm nên gap là 8, nhóm kế tiếp là 24. Đó là thang chia, không phải sở thích.”"),
       ("2. Hierarchy","Cái gì được đọc đầu tiên?",["Chỉ một thứ là primary.","4 đòn bẩy: size, weight, colour, space.","Nhấn mạnh có ngân sách cố định."],"“Status là primary. Nếu không thể to nhất thì phải có contrast cao nhất.”"),
       ("3. Type","Thứ tự đọc có còn đọc được không?",["3 cỡ chữ, 2 độ đậm, đều nằm trên scale.","Line height thuộc về cỡ chữ.","Cần cỡ thứ 4? Lỗi nằm ở Layer 2."],"“Ba cỡ, hai weight, đều trên scale. Cần cỡ thứ tư thì có gì đó phía trên đang sai.”"),
       ("4. Colour","Hành động chính là gì?",["Màu là vai trò, không phải bảng màu.","Primary là thứ duy nhất bão hoà.","Contrast: 4.5:1 chữ thường, 3:1 chữ lớn. Đo bằng tool."],"“Đỏ là role error. Dùng cho nút chính thì màn hình này không còn báo lỗi được.”"),
       ("5. Component","Vì sao nó tồn tại, khi nào không dùng?",["Component là lý lẽ được thừa hưởng.","Đủ 8 state: default đến empty.","Không resolve? Chạy lại 5 layer lên chính nó."],"“Button hiện có đã xử lý disabled và loading. Làm cái mới thì phải bảo trì hai cái mãi.”")]
    for i,(h,q,pts,dev) in enumerate(P):
        x=40+(i%3)*480;y=150+(i//3)*490
        b+=frame(x,y,450,460)+f'<line x1="{x}" y1="{y+60}" x2="{x+450}" y2="{y+60}" stroke="{INK}" stroke-width="1.5"/>'
        b+=f'<text x="{x+18}" y="{y+40}" {S} font-size="28" font-weight="700" fill="{INK}">{h}</text>'
        b+=f'<text x="{x+18}" y="{y+95}" {S} font-size="19" font-weight="600" fill="{AC}">{q}</text>'
        for k,p in enumerate(pts): b+=f'<text x="{x+18}" y="{y+130+k*26}" {S} font-size="17" fill="{INK}">{p}</text>'
        yy=y+235
        if i==0: b+=bar(x+30,yy,120,12,MU)+bar(x+30,yy+20,220)+bar(x+30,yy+54,120,12,MU)+bar(x+30,yy+74,220)+brk(x+300,yy+30,yy+54,"8")
        if i==1: b+=bar(x+30,yy,200,34,MU)+bar(x+30,yy+48,260)+f'<rect x="{x+30}" y="{yy+80}" width="130" height="38" rx="8" fill="{INK}"/>'
        if i==2: b+=bar(x+30,yy,180,26,INK)+bar(x+30,yy+40,240,14,MU)+bar(x+30,yy+66,300,8)+bar(x+30,yy+82,260,8)
        if i==3:
            for k,c in enumerate((AC,MU,"#2f9e6b","#e0a000","#d64545")): b+=f'<rect x="{x+30+k*76}" y="{yy}" width="60" height="50" rx="6" fill="none" stroke="{c}" stroke-width="3"/>'
        if i==4:
            for k in range(8): b+=f'<rect x="{x+30+k*50}" y="{yy}" width="40" height="28" rx="5" fill="{INK if k<7 else "none"}" stroke="{INK if k<7 else MU}" stroke-width="2"/>'
        b+=f'<text x="{x+18}" y="{y+390}" {S} font-size="16" font-style="italic" fill="{MU}">'
        # wrap dev sentence
        words=dev.split();lines=[];cur=""
        for w in words:
            if len(cur)+len(w)>46: lines.append(cur);cur=w
            else: cur=(cur+" "+w).strip()
        lines.append(cur)
        b+="".join(f'<tspan x="{x+18}" dy="{0 if j==0 else 22}">{l}</tspan>' for j,l in enumerate(lines))+'</text>'
    x,y=40+2*480,150+490
    b+=frame(x,y,450,460)+f'<line x1="{x}" y1="{y+60}" x2="{x+450}" y2="{y+60}" stroke="{INK}" stroke-width="1.5"/>'
    b+=f'<text x="{x+18}" y="{y+40}" {S} font-size="28" font-weight="700" fill="{INK}">6. Hai output</text>'
    L=[("Decision sheet","mỗi dòng: thay đổi gì, layer nào,",None),("","luật nào, câu nói với developer.",None),("Token audit","ghi lại những gì team đang dùng","(spacing, type, role), nêu chỗ lệch hoặc chưa định nghĩa."),("Nguyên tắc","Hỏi, đừng kết tội. “Mình chạy button qua","5 check, spacing và disabled chưa resolve. Anh/chị giải thích giúp mình lý do?”")]
    yy=y+100
    for hd,l1,l2 in L:
        if hd: b+=f'<text x="{x+18}" y="{yy}" {S} font-size="19" font-weight="600" fill="{AC}">{hd}</text>';yy+=26
        b+=f'<text x="{x+18}" y="{yy}" {S} font-size="17" fill="{INK}">{l1}</text>';yy+=24
        if l2: b+=f'<text x="{x+18}" y="{yy}" {S} font-size="17" fill="{INK}">{l2}</text>';yy+=24
        yy+=14
    svg(W,H,b,"ui-fundamentals-cheat-sheet.svg","cheat-sheets")
cheatsheet()
