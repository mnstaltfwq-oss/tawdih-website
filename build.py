# -*- coding: utf-8 -*-
import json, os, html, urllib.parse, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = os.path.dirname(os.path.abspath(__file__))
C = CONFIG
esc = html.escape
EN = {e[0]: e for e in ENTITIES}

ICONS = {
 "building": '<path d="M4 21V5l8-3 8 3v16M9 21v-4h6v4M8 9h2M14 9h2M8 13h2M14 13h2"/>',
 "file": '<path d="M6 2h9l5 5v15H6zM14 2v6h6M9 13h8M9 17h8"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6M16 4.5a3.5 3.5 0 010 7M22 21c0-3-1.5-5-4-5.7"/>',
 "check": '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5L16 9.5"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 "wa": '<path d="M3 21l1.6-5A8.5 8.5 0 1112 20.5a8.4 8.4 0 01-4-1z"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "pin": '<path d="M12 21s7-6.2 7-11a7 7 0 10-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "arrow": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 "tick": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "refresh": '<path d="M20 12a8 8 0 11-2.3-5.6M20 4v5h-5"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5zM3 13l9 5 9-5"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 "doc": '<path d="M6 2h9l5 5v15H6zM14 2v6h6M9 13h8M9 17h5"/>',
}
def raw(n,cls=''): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'
def icon(n): return f'<span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONS[n]}</svg></span>'

def wa(text=""):
    u = f"https://wa.me/{C['wa']}"
    return u + ("?text=" + urllib.parse.quote(text) if text else "")

NAV = [("index.html","الرئيسية"),("about.html","من نحن"),("services.html","خدماتنا"),("packages.html","باقات الأعمال"),
       ("platforms-management.html","إدارة المنصات"),("projects.html","المشاريع والفرص"),("contact.html","تواصل معنا")]

HERO_SVG = '''<svg viewBox="0 0 520 400" role="img" aria-label="رسم توضيحي لوحة متابعة إجراءات المنشأة">
<defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#003090"/><stop offset="1" stop-color="#0080E0"/></linearGradient></defs>
<rect x="20" y="30" width="480" height="340" rx="22" fill="#F4F8FC" stroke="#dbe5f1"/>
<rect x="20" y="30" width="480" height="48" rx="22" fill="#001050"/><rect x="20" y="56" width="480" height="22" fill="#001050"/>
<circle cx="478" cy="54" r="6" fill="#00B0A0"/><circle cx="458" cy="54" r="6" fill="#00B0F0"/><circle cx="438" cy="54" r="6" fill="#fff" opacity=".6"/>
<rect x="300" y="98" width="180" height="120" rx="16" fill="url(#g1)"/>
<path d="M322 190l30-34 24 20 36-46 40 28" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="40" y="98" width="240" height="56" rx="14" fill="#fff" stroke="#dbe5f1"/><circle cx="256" cy="126" r="14" fill="#00B0A0"/><path d="M249 126l5 5 9-10" stroke="#001050" stroke-width="3" fill="none" stroke-linecap="round"/><rect x="70" y="112" width="140" height="10" rx="5" fill="#001050"/><rect x="100" y="132" width="110" height="8" rx="4" fill="#b9c7da"/>
<rect x="40" y="166" width="240" height="56" rx="14" fill="#fff" stroke="#dbe5f1"/><circle cx="256" cy="194" r="14" fill="#00B0A0"/><path d="M249 194l5 5 9-10" stroke="#001050" stroke-width="3" fill="none" stroke-linecap="round"/><rect x="70" y="180" width="120" height="10" rx="5" fill="#001050"/><rect x="90" y="200" width="120" height="8" rx="4" fill="#b9c7da"/>
<rect x="40" y="234" width="240" height="56" rx="14" fill="#fff" stroke="#dbe5f1"/><circle cx="256" cy="262" r="14" fill="#00B0F0"/><rect x="249" y="258" width="14" height="8" rx="2" fill="#fff"/><rect x="70" y="248" width="150" height="10" rx="5" fill="#001050"/><rect x="110" y="268" width="100" height="8" rx="4" fill="#b9c7da"/>
<rect x="300" y="234" width="180" height="56" rx="14" fill="#fff" stroke="#dbe5f1"/><rect x="320" y="250" width="100" height="10" rx="5" fill="#001050"/><rect x="360" y="270" width="60" height="8" rx="4" fill="#b9c7da"/><circle cx="450" cy="262" r="12" fill="#0080E0"/>
<rect x="40" y="304" width="440" height="40" rx="12" fill="#fff" stroke="#dbe5f1"/><rect x="60" y="318" width="200" height="10" rx="5" fill="#b9c7da"/><rect x="380" y="312" width="86" height="24" rx="12" fill="#00B0A0"/>
</svg>'''

def head(title, desc, active="", depth_note=""):
    full = f"{title} | توضيح المعرفة لخدمات الأعمال" if title != "الرئيسية" else "توضيح المعرفة لخدمات الأعمال | خدمات أعمال إدارية وتشغيلية من حائل لجميع مناطق المملكة"
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#001050">
<meta property="og:title" content="{esc(full)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:locale" content="ar_SA"><meta property="og:type" content="website">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
<div class="topbar"><div class="wrap"><a href="tel:{C['phone_tel']}" dir="ltr">{raw('phone')}{C['phone_display']}</a><span>{raw('pin')}حائل، المملكة العربية السعودية</span><span class="hide-m">{raw('clock')}خدماتنا عن بُعد لجميع مناطق المملكة</span></div></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="index.html" aria-label="توضيح المعرفة لخدمات الأعمال - الرئيسية"><img src="logo.png" alt="شعار توضيح المعرفة لخدمات الأعمال" width="160" height="54"></a>
<nav id="nav" class="nav" aria-label="القائمة الرئيسية">{nav}</nav>
<a class="btn btn-p btn-top" href="{wa('السلام عليكم، أرغب في طلب خدمة من توضيح المعرفة لخدمات الأعمال.')}" target="_blank" rel="noopener">{raw('wa')}اطلب خدمتك</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">القائمة</button>
</div></header>
<main id="main">
'''

def foot():
    mail = f'<a href="mailto:{C["email"]}">{C["email"]}</a>' if C["email"] else ""
    return f'''</main>
<footer class="ftr"><div class="wrap">
<div class="cols">
<div><span class="logo-w"><img src="logo.png" alt="توضيح المعرفة لخدمات الأعمال" width="140" height="46"></span>
<p>شركة سعودية مقرها حائل، تقدم خدمات الأعمال الإدارية والتشغيلية ومتابعة الإجراءات والمنصات الحكومية للمنشآت ورواد الأعمال والمستثمرين.</p><p class="slogan">أعمالك تستحق وقتك.. وإجراءاتها علينا.</p></div>
<div><h3>خدمات مختارة</h3><a href="entity-business-center.html">تأسيس الشركات</a><a href="entity-qiwa.html">خدمات منصة قوى</a><a href="entity-misa.html">خدمات وزارة الاستثمار</a><a href="entity-balady.html">خدمات منصة بلدي</a><a href="entity-gosi.html">خدمات التأمينات الاجتماعية</a><a href="entity-zatca.html">خدمات الزكاة والضريبة</a><a href="platforms-management.html">إدارة المنصات الحكومية</a></div>
<div><h3>روابط سريعة</h3><a href="index.html">الرئيسية</a><a href="about.html">من نحن</a><a href="services.html">الخدمات</a><a href="packages.html">باقات الأعمال</a><a href="faq.html">الأسئلة الشائعة</a><a href="contact.html">تواصل معنا</a><a href="privacy.html">سياسة الخصوصية</a><a href="terms.html">الشروط والأحكام</a></div>
<div><h3>تواصل معنا</h3><span>{C['city']}</span><a href="tel:{C['phone_tel']}" dir="ltr" style="text-align:right">{C['phone_display']}</a><a href="{wa()}" target="_blank" rel="noopener">واتساب</a>{mail}<span>نطاق الخدمة: جميع مناطق المملكة</span></div>
</div>
<div class="disc"><p><a style="display:inline" href="refund.html">سياسة الإلغاء والاسترجاع</a></p>
<p><strong>تنويه:</strong> شركة توضيح المعرفة جهة خاصة تقدم خدمات أعمال مساندة، وليست جهة حكومية ولا تمثل الجهات والمنصات الرسمية المذكورة في الموقع. أسماء الجهات والمنصات تُذكر للتعريف بالخدمة فقط، وتعود ملكيتها لأصحابها.</p>
<p>© 2026 شركة توضيح المعرفة لخدمات الأعمال. جميع الحقوق محفوظة.</p></div>
</div></footer>
<script src="app.js" defer></script>
</body></html>'''

def page(fn, title, desc, body, active=""):
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(head(title, desc, active) + body + foot())
    PAGES.append(fn)
PAGES = []

def phero(title, desc, crumbs):
    c = " › ".join(f'<a href="{h}">{t}</a>' if h else t for t, h in crumbs)
    return f'<section class="page-hero"><div class="wrap"><div class="crumbs">{c}</div><h1>{title}</h1><p class="lead" style="max-width:780px;margin:0">{desc}</p></div></section>'

def cta(t="جاهز لبدء طلبك؟", d="أرسل لنا احتياجك عبر واتساب ويراجعه فريقنا ويحدد معك الخطوة التالية."):
    return f'<section class="s"><div class="wrap"><div class="cta"><div><h2>{t}</h2><p>{d}</p></div><a class="btn btn-wa" href="{wa("السلام عليكم، أرغب في طلب خدمة من توضيح المعرفة لخدمات الأعمال.")}" target="_blank" rel="noopener">اطلب خدمتك عبر واتساب</a></div></div></section>'

# ---------------- الرئيسية
HOME_ENTS = ["business-center","mc","misa","qiwa","balady","gosi","zatca","mim","mofa","absher-business","saip","chambers"]
ent_cards = "".join(f'<a class="card hov ent" href="entity-{EN[k][0]}.html"><span class="mono" aria-hidden="true">{EN[k][2]}</span><h3>{EN[k][1]}</h3><p>{EN[k][3]}</p><span class="more">عرض الخدمات {raw("arrow")}</span></a>' for k in HOME_ENTS)
WHY = [("خبرة عملية","نساعد أصحاب المنشآت على فهم الإجراءات الحكومية وتنظيم خطوات تنفيذها.","target"),
       ("خدمات للمنشآت والمستثمرين","نقدم خدماتنا لرواد الأعمال والشركات والمستثمرين داخل المملكة.","users"),
       ("جهات متعددة في مكان واحد","نجمع خدمات تأسيس الأعمال والموظفين والتراخيص والمنصات الحكومية.","layers"),
       ("متابعة مستمرة","نساعدك على متابعة الطلبات والمواعيد والتجديدات بحسب نطاق الخدمة.","refresh")]
why = "".join(f'<article class="card"><span class="ic" aria-hidden="true">{raw(i)}</span><h3>{t}</h3><p>{d}</p></article>' for t,d,i in WHY)
CONSULT = [("التشخيص والإرشاد","نساعدك على تحديد الإجراء المناسب لمنشأتك وفهم متطلبات الجهة الحكومية ذات العلاقة.","search"),
           ("دراسة متطلبات التأسيس","نراجع طبيعة النشاط والإجراءات المرتبطة بتأسيس المنشأة وتجهيزها لبدء العمل.","building"),
           ("الامتثال والجاهزية","نساعدك على مراجعة التراخيص والالتزامات الإدارية والتنظيمية المتعلقة بنشاط منشأتك.","check"),
           ("التنفيذ والمتابعة","نتولى متابعة الإجراءات المتفق عليها عبر القنوات الرسمية، مع اطلاعك على حالة الطلب والمستندات المطلوبة.","doc")]
consult = "".join(f'<article class="card"><span class="ic" aria-hidden="true">{raw(i)}</span><h3>{t}</h3><p>{d}</p></article>' for t,d,i in CONSULT)
home_faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in FAQ)
home_ld = json.dumps({"@context":"https://schema.org","@graph":[
  {"@type":"ProfessionalService","name":"شركة توضيح المعرفة لخدمات الأعمال","slogan":"أعمالك تستحق وقتك.. وإجراءاتها علينا.","telephone":C["phone_tel"],"address":{"@type":"PostalAddress","addressLocality":"حائل","addressCountry":"SA"},"areaServed":"SA","url":C["base_url"]},
  {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}]},ensure_ascii=False)
WA_MSG = wa('السلام عليكم، أرغب في طلب خدمة من توضيح المعرفة لخدمات الأعمال.')
body = f'''<section class="hero"><div class="wrap">
<div><span class="tag">حلول متكاملة لإدارة خدمات منشأتك الحكومية</span>
<h1>أعمالك تستحق وقتك.. وإجراءاتها علينا.</h1>
<p class="lead">من تأسيس شركتك وإصدار التراخيص إلى إدارة الموظفين والمنصات الحكومية، تساعدك توضيح المعرفة على إنجاز إجراءات منشأتك ومتابعتها من مكان واحد، بخطوات واضحة وخدمة مهنية.</p>
<div class="acts"><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener">{raw("wa")}اطلب خدمتك عبر واتساب</a><a class="btn btn-o" href="services.html">تصفّح خدماتنا</a></div>
<ul class="ticks"><li>{raw("tick")}استشارة أولية لفهم احتياجك</li><li>{raw("tick")}خصوصية مستندات منشأتك</li><li>{raw("tick")}خدمات عن بُعد لجميع مناطق المملكة</li></ul></div>
<div class="hero-art">{HERO_SVG}</div></div></section>

<section class="stats" aria-label="توضيح المعرفة بالأرقام"><div class="wrap"><div class="box-s">
<div class="stat"><b>{len(ENTITIES)}</b><span>جهة ومنصة حكومية</span></div>
<div class="stat"><b>3</b><span>باقات أعمال</span></div>
<div class="stat"><b>13</b><span>منطقة نخدمها عن بُعد</span></div>
<div class="stat"><b>مجاني</b><span>فحص أولي لاحتياجك</span></div>
</div></div></section>

<section class="s"><div class="wrap"><div class="s-head"><span class="eyebrow">خدمات الأعمال</span><h2>خدمات الوزارات والجهات الحكومية</h2><p class="lead">اختر الجهة المختصة لتعرف خدماتها، ثم اطلب الخدمة التي تحتاجها عبر واتساب.</p></div>
<div class="grid g4">{ent_cards}</div><p style="margin-top:28px"><a class="btn btn-p" href="services.html">عرض جميع الجهات {raw("arrow")}</a></p></div></section>

<section class="s alt"><div class="wrap split">
<div><span class="eyebrow">الاستشارات الحكومية</span><h2>استشارات تساعدك على اتخاذ الخطوة الصحيحة</h2>
<p class="lead">سواء كنت تستعد لتأسيس منشأتك أو تحتاج إلى معالجة إجراء حكومي قائم، نساعدك على فهم المتطلبات وتحديد الخطوات المناسبة قبل البدء.</p>
<ul class="ticks"><li>{raw("tick")}توضيح الإجراءات والمتطلبات</li><li>{raw("tick")}تحديد الجهات والمنصات المختصة</li><li>{raw("tick")}تنظيم خطوات التنفيذ والمتابعة</li></ul>
<div class="acts" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px"><a class="btn btn-p" href="{WA_MSG}" target="_blank" rel="noopener">اطلب استشارتك الأولية</a><a class="btn btn-o" href="readiness.html">فحص جاهزية المنشأة</a></div></div>
<div class="mini">{consult}</div></div></section>

<section class="s"><div class="wrap"><div class="s-head"><span class="eyebrow">لماذا توضيح المعرفة؟</span><h2>شريك واضح في إجراءات منشأتك</h2></div>
<div class="grid g4">{why}</div></div></section>

<section class="s alt"><div class="wrap"><div class="s-head"><span class="eyebrow">كيف نعمل؟</span><h2>من طلبك إلى إكمال الخدمة في أربع خطوات</h2></div>
<ol class="steps"><li><h3>اطلب خدمتك</h3><p>تواصل معنا عبر واتساب وحدد الخدمة أو الإجراء الذي تحتاجه منشأتك.</p></li><li><h3>مراجعة المتطلبات</h3><p>نراجع تفاصيل الطلب ونوضح المستندات والاشتراطات والخطوات اللازمة.</p></li><li><h3>التنفيذ والمتابعة</h3><p>نبدأ تنفيذ الإجراءات المتفق عليها ومتابعتها عبر الجهات والمنصات الرسمية.</p></li><li><h3>إكمال الخدمة</h3><p>نبلغك بنتيجة الطلب ونسلمك المستندات المتاحة بعد اكتمال الإجراء.</p></li></ol></div></section>

<section class="s"><div class="wrap faq-wrap"><div class="s-head center"><span class="eyebrow">الأسئلة الشائعة</span><h2>إجابات تساعدك قبل طلب الخدمة</h2></div>{home_faq}
<p style="text-align:center;margin-top:20px"><a class="more" href="faq.html">كل الأسئلة الشائعة {raw("arrow")}</a></p></div></section>

<section class="s"><div class="wrap"><div class="cta"><div><h2>جاهز لتنظيم وإنجاز إجراءات منشأتك؟</h2><p>من تأسيس الأعمال إلى إدارة الموظفين والتراخيص والمنصات الحكومية، نساعدك على تحديد الخدمة المناسبة ومتابعة إجراءاتها بخطوات واضحة.</p><p class="slogan">أعمالك تستحق وقتك.. وإجراءاتها علينا.</p></div>
<div class="acts"><a class="btn btn-wa" href="{WA_MSG}" target="_blank" rel="noopener">{raw("wa")}اطلب خدمتك عبر واتساب</a><a class="btn btn-ol" href="contact.html">أرسل طلبك</a></div></div></div></section>
<script type="application/ld+json">{home_ld}</script>'''
page("index.html","الرئيسية","تأسيس الشركات والمؤسسات، إدارة المنصات الحكومية، التراخيص والموارد البشرية وتأهيل المنشآت للمشاريع. شركة سعودية مقرها حائل.",body,"index.html")

# ---------------- من نحن
body = phero("توضيح المعرفة.. شريكك في إدارة إجراءات أعمالك.","شركة سعودية مقرها حائل، متخصصة في تقديم خدمات الأعمال الإدارية والتشغيلية للشركات والمؤسسات ورواد الأعمال والمستثمرين.",[("الرئيسية","index.html"),("من نحن",None)]) + f'''
<section class="s"><div class="wrap prose"><p>شركة توضيح المعرفة لخدمات الأعمال شركة سعودية مقرها حائل، متخصصة في تقديم خدمات الأعمال الإدارية والتشغيلية للشركات والمؤسسات ورواد الأعمال والمستثمرين.</p>
<p>نساعد المنشآت في تأسيس أعمالها ومتابعة إجراءاتها الحكومية وإدارة خدمات المنصات والتراخيص والموارد البشرية، إلى جانب تنظيم متطلبات التأهيل للمشاريع والمنافسات.</p>
<p>نعمل على تقديم خدمات واضحة ومنظمة تساعد أصحاب المنشآت على متابعة التزاماتهم وتوفير الوقت والجهد.</p></div></section>
<section class="s alt"><div class="wrap"><div class="grid g2"><article class="card"><h3>الرؤية</h3><p>أن نكون شريكًا موثوقًا للمنشآت في إدارة الإجراءات الحكومية والتشغيلية ورفع جاهزيتها للنمو.</p></article>
<article class="card"><h3>الرسالة</h3><p>تقديم خدمات أعمال متكاملة تساعد المنشآت على تنظيم إجراءاتها ومتابعة متطلباتها والالتزام بالأنظمة ذات العلاقة.</p></article></div>
<div class="s-head" style="margin-top:40px"><h2>قيمنا</h2></div>
<div class="grid g3">{"".join(f'<article class="card"><h3>{v}</h3></article>' for v in ["الثقة","الاحترافية","الشفافية","التنظيم","الالتزام","التحسين المستمر"])}</div></div></section>
<section class="s"><div class="wrap"><div class="note"><strong>توضيح مهم:</strong> توضيح المعرفة جهة خاصة وليست جهة حكومية، ولا تضمن قرارات الجهات المختصة. دورنا تجهيز الطلبات ومتابعتها وتنظيمها وفق المتطلبات المعلنة.</div></div></section>{cta()}'''
page("about.html","من نحن","شركة توضيح المعرفة لخدمات الأعمال: شركة سعودية مقرها حائل تقدم خدمات الأعمال الإدارية والتشغيلية للمنشآت.",body,"about.html")

# ---------------- الخدمات الحكومية
cats = sorted({e[4] for e in ENTITIES})
opts = "".join(f'<option value="{c}">{c}</option>' for c in cats)
ent_all = "".join(f'<a class="card" style="text-decoration:none" href="entity-{e[0]}.html" data-filter data-cat="{e[4]}" data-text="{esc(e[1]+" "+e[3]+" "+e[4])}"><span class="mono" aria-hidden="true">{e[2]}</span><h3>{e[1]}</h3><p>{e[3]}</p><span style="color:var(--blue-d);font-weight:600">استعرض الخدمات ←</span></a>' for e in ENTITIES)
svc_all = "".join(f'<article class="card" data-filter data-cat="{EN[s["entity"]][4]}" data-text="{esc(s["name"]+" "+s["platform"]+" "+s["description"])}"><span class="tag">{esc(s["platform"])}</span><h3>{esc(s["name"])}</h3><p>{esc(s["description"][:130])}…</p><div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn btn-o btn-sm" href="service-{s["id"]}.html">تفاصيل الخدمة</a></div></article>' for s in SERVICES)
body = phero("الخدمات الحكومية والإلكترونية للمنشآت.","استعرض الخدمات الحكومية بحسب الوزارة أو المنصة المختصة، وتعرف على طبيعة كل خدمة ومتطلبات تقديمها والمستندات اللازمة لتنفيذها.",[("الرئيسية","index.html"),("الخدمات الحكومية",None)]) + f'''
<section class="s"><div class="wrap">
<div class="tools" role="search"><label class="sr" for="q">ابحث عن جهة أو خدمة</label><input id="q" type="search" placeholder="ابحث عن جهة أو خدمة..."><label class="sr" for="cat">التصنيف</label><select id="cat"><option value="">كل التصنيفات</option>{opts}</select></div>
<h2>الجهات والمنصات</h2><div class="grid g3" style="margin-bottom:40px">{ent_all}</div>
<h2>الخدمات المنشورة</h2><div class="grid g3">{svc_all}</div>
<div id="empty" class="empty" role="status">لا توجد نتائج مطابقة. جرّب كلمة أخرى أو <a href="{wa('السلام عليكم، أبحث عن خدمة ولم أجدها في الموقع.')}" target="_blank" rel="noopener">اسألنا عبر واتساب</a>.</div>
<div class="note" style="margin-top:28px">نضيف الخدمات تدريجيًا بعد مطابقتها مع المصادر الرسمية. لا نعرض إلا ما أمكن توثيقه، ويمكنك دائمًا الاستفسار عن أي خدمة غير مدرجة عبر واتساب.</div>
</div></section>{cta()}'''
page("services.html","الخدمات الحكومية","استعرض الخدمات الحكومية بحسب الوزارة أو المنصة: قوى، أجير، مُدد، التأمينات، بلدي، الزكاة والضريبة وغيرها.",body,"services.html")

# ---------------- صفحات الجهات
for e in ENTITIES:
    sv = [s for s in SERVICES if s["entity"] == e[0]]
    if sv:
        cs = "".join(f'<article class="card"><h3>{esc(s["name"])}</h3><p>{esc(s["description"][:150])}…</p><div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn btn-o btn-sm" href="service-{s["id"]}.html">تفاصيل الخدمة</a><a class="btn btn-p btn-sm" href="{wa("السلام عليكم، أرغب في طلب خدمة: "+s["name"]+" - الجهة: "+e[1])}" target="_blank" rel="noopener">اطلب الخدمة</a></div></article>' for s in sv)
        main = f'<div class="grid g3">{cs}</div><div class="note" style="margin-top:22px">نضيف بقية خدمات {e[1]} تدريجيًا بعد توثيقها من المصادر الرسمية. تواصل معنا إن كانت خدمتك غير مدرجة.</div>'
    else:
        main = f'<div class="box"><h2>قيد استكمال التوثيق</h2><p>نعمل على توثيق خدمات {e[1]} من مصادرها الرسمية قبل نشرها، ولا ننشر اشتراطات أو مستندات من التخمين. يمكنك الآن إرسال استفسارك وسيحدد فريقنا معك المتطلبات.</p></div>'
    side = f'<aside class="side" aria-label="طلب خدمة"><h3>تحتاج خدمة من {e[1]}؟</h3><p>نساعدك في تحديد متطلبات الخدمة ومراجعة المستندات اللازمة ومتابعة إجراءات الطلب.</p><a class="btn btn-wa" href="{wa("السلام عليكم، أحتاج خدمة من "+e[1])}" target="_blank" rel="noopener">اطلب الخدمة عبر واتساب</a></aside>'
    body = phero(f"خدمات {e[1]}", f"نقدم خدمات مساندة للمنشآت في متابعة الإجراءات المتاحة عبر {e[1]}. {e[3]}", [("الرئيسية","index.html"),("الخدمات الحكومية","services.html"),(e[1],None)]) + f'<section class="s"><div class="wrap two"><div>{main}</div>{side}</div></section>'
    page(f"entity-{e[0]}.html", f"خدمات {e[1]}", f"خدمات {e[1]} للمنشآت: {e[3]}", body, "services.html")

# ---------------- صفحات الخدمات
def list_or_missing(v, ordered=False):
    if not v:
        return '<p class="note">لم تنشر الجهة المختصة هذا القسم نصًّا في صفحة الخدمة وقت المراجعة، ولذلك لا نضع بديلًا من التخمين. راجع الرابط الرسمي أدناه، وسنؤكد لك القائمة النهائية قبل البدء بالطلب.</p>'
    t = "ol" if ordered else "ul"
    return f'<{t}>' + "".join(f"<li>{esc(x)}</li>" for x in v) + f'</{t}>'
for s in SERVICES:
    e = EN[s["entity"]]
    msg = f"السلام عليكم، أرغب في طلب خدمة: {s['name']} - الجهة: {e[1]}"
    out = esc(s["outputs"]) if s["outputs"] else '<span class="note" style="display:block">لم تنشر الجهة قسم المخرجات نصًّا وقت المراجعة.</span>'
    body = phero(esc(s["name"]), f'{esc(s["platform"])} · حالة التوثيق: {s["status"]}', [("الرئيسية","index.html"),("الخدمات الحكومية","services.html"),(e[1],f"entity-{e[0]}.html"),(s["name"],None)]) + f'''
<section class="s"><div class="wrap two"><div>
<div class="meta"><div><b>الجهة المختصة</b>{esc(e[1])}</div><div><b>منصة التنفيذ</b>{esc(s["platform"])}</div><div><b>آخر مراجعة</b>{s["reviewed"]}</div><div><b>حالة التوثيق</b>{s["status"]}</div></div>
<div class="box"><h2>وصف الخدمة</h2><p>{esc(s["description"])}</p><p><strong>لمن تُقدَّم؟</strong> {esc(s["audience"])}</p><p><strong>متى تحتاجها؟</strong> {esc(s["when"])}</p><p><strong>دور توضيح المعرفة:</strong> نساعدك في مراجعة احتياج منشأتك وتجهيز بيانات الطلب ومتابعة إجراءاته مع الجهة المختصة، دون ضمان قرار الجهة.</p></div>
<div class="box"><h2>متطلبات الخدمة</h2>{list_or_missing(s["requirements"])}</div>
<div class="box"><h2>المستندات المطلوبة</h2>{list_or_missing(s["documents"])}</div>
<div class="box"><h2>مخرجات الخدمة</h2><p>{out}</p></div>
<div class="box"><h2>خطوات التقديم</h2>{list_or_missing(s["steps"], True)}</div>
<div class="box"><h2>المصدر الرسمي</h2><p>{esc(s["source_name"])}: <a href="{s["source"]}" target="_blank" rel="noopener">صفحة الخدمة لدى الجهة</a></p></div>
</div>
<aside class="side"><h3>اطلب هذه الخدمة</h3><p>{esc(s["name"])} — {esc(e[1])}</p><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">اطلب الخدمة عبر واتساب</a></aside></div></section>'''
    page(f"service-{s['id']}.html", s["name"], f'{s["name"]} - {e[1]}. {s["description"][:120]}', body, "services.html")

# ---------------- الباقات
def yn(v): return '<span class="y" aria-label="مشمولة">✓ مشمولة</span>' if v else '<span class="n" aria-label="غير مشمولة">— غير مشمولة</span>'
rows = [("المساعدة في متطلبات التأسيس وتجهيز البيانات",1,1,1),("متابعة السجل التجاري ووثائق الكيان",1,1,1),("التجهيز التشغيلي للمنشأة",0,1,1),("التراخيص والمنصات الحكومية بحسب النشاط",0,1,1),("فحص جاهزية المشاريع",0,0,1),("تنظيم ملفات التأهيل للمنافسات",0,0,1),("متابعة الفرص المناسبة",0,0,1)]
tbl = "".join(f"<tr><td>{r[0]}</td><td>{yn(r[1])}</td><td>{yn(r[2])}</td><td>{yn(r[3])}</td></tr>" for r in rows)
pk = [("الانطلاقة","مخصصة لتأسيس الشركات والمؤسسات.","تشمل المساعدة في متطلبات التأسيس وتجهيز البيانات ومتابعة السجل التجاري ووثائق الكيان."),("التشغيل","مخصصة للمنشآت التي ترغب في استكمال متطلبات بدء النشاط.","تشمل خدمات التأسيس والتجهيز التشغيلي والتراخيص والمنصات الحكومية بحسب النشاط."),("التمكين","مخصصة للمنشآت التي تستهدف التوسع والمشاريع.","تشمل خدمات التشغيل، إضافة إلى فحص جاهزية المشاريع وتنظيم ملفات التأهيل ومتابعة الفرص.")]
pc = "".join(f'<article class="card"><span class="tag">{"الباقة "+n}</span><h3>{t}</h3><p><strong>{d}</strong></p><p>{x}</p><a class="btn btn-wa btn-sm" href="{wa("السلام عليكم، أرغب في الاستفسار عن باقة "+t)}" target="_blank" rel="noopener">استفسر عن الباقة</a></article>' for n,(t,d,x) in zip(["الأولى","الثانية","الثالثة"],pk))
body = phero("باقات أعمال تناسب كل مرحلة من مراحل منشأتك.","اختر الباقة المناسبة لاحتياج منشأتك، من التأسيس إلى تجهيز التشغيل والاستعداد للمشاريع والمنافسات.",[("الرئيسية","index.html"),("باقات الأعمال",None)]) + f'''
<section class="s"><div class="wrap"><div class="grid g3">{pc}</div>
<div class="s-head" style="margin-top:48px"><h2>مقارنة الباقات</h2></div>
<div class="tw"><table><caption class="sr">مقارنة الخدمات المشمولة في الباقات</caption><thead><tr><th>الخدمة</th><th>الانطلاقة</th><th>التشغيل</th><th>التمكين</th></tr></thead><tbody>{tbl}</tbody></table></div>
<div class="box" style="margin-top:24px"><h2>ما لا تشمله الباقات</h2><ul><li>الرسوم الحكومية، وتُسدَّد للجهة المختصة بشكل منفصل.</li><li>ضمان موافقة الجهات الحكومية على الطلبات أو ترسية المنافسات.</li><li>الخدمات الإضافية خارج النطاق المتفق عليه، ويمكن طلبها بشكل مستقل.</li></ul></div></div></section>{cta("لست متأكدًا من الباقة المناسبة؟","أخبرنا بنشاط منشأتك ومرحلتها وسنرشح لك الأنسب.")}'''
page("packages.html","باقات الأعمال","باقات توضيح المعرفة: الانطلاقة للتأسيس، التشغيل لبدء النشاط، التمكين للتوسع والمشاريع.",body,"packages.html")

# ---------------- إدارة المنصات
plans = [("الإدارة الأساسية","مناسبة للمنشآت الصغيرة التي تحتاج إلى متابعة عدد محدود من المنصات والطلبات.","عدد محدود من المنصات يُحدد في الاتفاق","طلبات دورية بسيطة","متابعة الطلبات المتفق عليها فقط","تقرير موجز بحسب الاتفاق"),
 ("الإدارة المتقدمة","مناسبة للمنشآت النامية التي تتعدد لديها الإجراءات والموظفون والالتزامات.","عدد أوسع من المنصات يُحدد في الاتفاق","طلبات متعددة تشمل شؤون الموظفين والتجديدات","متابعة الطلبات والملاحظات والمواعيد","تقارير دورية بحسب الاتفاق"),
 ("الإدارة الشاملة","مناسبة للشركات التي تحتاج إلى تنسيق ومتابعة نطاق أوسع من المنصات والإجراءات.","نطاق واسع من المنصات يُحدد في الاتفاق","طلبات متنوعة عبر عدة جهات","تنسيق ومتابعة شاملة ضمن النطاق المتفق عليه","تقارير دورية موسعة بحسب الاتفاق")]
pl = "".join(f'<article class="card"><h3>{p[0]}</h3><p>{p[1]}</p></article>' for p in plans)
pt = "".join(f"<tr><th scope='row' style='background:var(--bg);color:var(--navy)'>{h}</th>" + "".join(f"<td>{p[i]}</td>" for p in plans) + "</tr>" for h,i in [("المنصات المشمولة",2),("نوع الطلبات",3),("حدود المتابعة",4),("دورية التقارير",5)])
body = phero("إدارة منصات منشأتك الحكومية.. متابعة منظمة لأعمالك.","تعدد المنصات الحكومية والالتزامات الدورية قد يستهلك وقت صاحب المنشأة ويزيد من صعوبة متابعة الطلبات والتجديدات.",[("الرئيسية","index.html"),("إدارة المنصات",None)]) + f'''
<section class="s"><div class="wrap"><div class="prose"><p>تساعدك شركة توضيح المعرفة في تنظيم خدمات منشأتك الحكومية، ومتابعة الطلبات والملاحظات والمستندات والالتزامات، وتقديم تقارير دورية ضمن نطاق إدارة متفق عليه.</p></div>
<div class="grid g3" style="margin:28px 0">{pl}</div>
<div class="tw"><table><caption class="sr">مقارنة خطط الإدارة</caption><thead><tr><th>البند</th><th>الأساسية</th><th>المتقدمة</th><th>الشاملة</th></tr></thead><tbody>{pt}</tbody></table></div>
<div class="grid g2" style="margin-top:24px"><div class="box"><h2>الخدمات المستثناة</h2><ul><li>الرسوم الحكومية والغرامات.</li><li>أي منصة أو إجراء خارج النطاق المكتوب في الاتفاق.</li><li>ضمان قرارات الجهات المختصة.</li></ul></div>
<div class="box"><h2>طلب خدمات إضافية</h2><p>يمكنك طلب أي خدمة خارج نطاق خطتك في أي وقت عبر واتساب، فنقدّر نطاقها ونرسل لك تفاصيلها مكتوبة، ولا يبدأ التنفيذ إلا بموافقتك.</p></div></div></div></section>{cta("اطلب خطة إدارة تناسب منشأتك")}'''
page("platforms-management.html","إدارة المنصات الحكومية","خطط إدارة المنصات الحكومية للمنشآت: أساسية ومتقدمة وشاملة مع تقارير دورية ونطاق واضح.",body,"platforms-management.html")

# ---------------- المشاريع
body = phero("المشاريع والفرص.. استعد قبل أن تتنافس.","نساعد المنشآت في متابعة المنافسات الحكومية والفرص الاستثمارية وفرص التوريد والمقاولات المناسبة لأنشطتها.",[("الرئيسية","index.html"),("المشاريع والفرص",None)]) + f'''
<section class="s"><div class="wrap"><div class="grid g3">
<article class="card"><h3>متابعة الفرص</h3><p>رصد المنافسات والفرص المناسبة لنشاط منشأتك عبر منصات مثل اعتماد وفرص.</p></article>
<article class="card"><h3>تنظيم ملفات التأهيل</h3><p>تجهيز المستندات اللازمة للمشاركة وترتيبها وفق متطلبات كل منافسة.</p></article>
<article class="card"><h3>فحص الجاهزية</h3><p>مراجعة جاهزية المنشأة وتحديد الفجوات قبل التقديم.</p><a class="btn btn-o btn-sm" href="readiness.html">افحص جاهزية منشأتك</a></article></div>
<p class="note" style="margin-top:24px">خدماتنا مساندة وتنظيمية، ولا نضمن ترسية أي منافسة أو قبول أي طلب تأهيل.</p></div></section>{cta()}'''
page("projects.html","المشاريع والفرص","متابعة المنافسات الحكومية والفرص وتأهيل المنشآت للمشاريع وتنظيم ملفات المشاركة.",body,"projects.html")

checks = ["السجل التجاري ساري ومطابق للنشاط","شهادة الزكاة والضريبة والدخل سارية","شهادة التأمينات الاجتماعية سارية","شهادة الالتزام بالتوطين (نطاقات) سارية","الرخص البلدية والتراخيص المرتبطة بالنشاط سارية","عضوية الغرفة التجارية سارية","تصنيف المقاولين (إن كان النشاط مقاولات)","القوائم المالية والخبرات السابقة"]
cl = "".join(f'<li><label><input type="checkbox" class="chk"> {c}</label></li>' for c in checks)
body = phero("فحص جاهزية المنشأة للمشاريع والمنافسات.","قائمة مراجعة مبدئية تساعدك على معرفة ما يلزم تجهيزه قبل التقدم للمنافسات. المتطلبات النهائية تحددها كل منافسة.",[("الرئيسية","index.html"),("فحص الجاهزية",None)]) + f'''
<section class="s"><div class="wrap two"><div class="box"><h2>قائمة المراجعة المبدئية</h2><ul style="list-style:none;padding:0" id="cl">{cl}</ul><p id="score" role="status" style="font-weight:600;color:var(--navy)"></p>
<p class="note">هذه القائمة استرشادية وليست قانونية ولا تغني عن مراجعة كراسة شروط كل منافسة.</p></div>
<aside class="side"><h3>راجع جاهزيتك معنا</h3><p>نراجع وضع منشأتك ونحدد معك ما ينقصها قبل التقديم.</p><a class="btn btn-wa" href="{wa("السلام عليكم، أرغب في فحص جاهزية منشأتي للمشاريع والمنافسات.")}" target="_blank" rel="noopener">اطلب فحص الجاهزية</a></aside></div></section>
<script>(function(){{var b=document.querySelectorAll('.chk'),s=document.getElementById('score');function u(){{var n=0;b.forEach(function(x){{if(x.checked)n++}});s.textContent='أنجزت '+n+' من '+b.length+' بنود';}}b.forEach(function(x){{x.addEventListener('change',u)}});u();}})();</script>'''
page("readiness.html","فحص جاهزية المنشأة","قائمة مراجعة مبدئية لفحص جاهزية منشأتك للمشاريع والمنافسات الحكومية.",body,"projects.html")

# ---------------- المستثمرون
body = phero("خدمات المستثمرين.. ابدأ نشاطك في المملكة بخطوات منظمة.","نساعد المستثمرين ورواد الأعمال في تنظيم إجراءات الدخول وبدء النشاط ومتابعة المتطلبات مع الجهات المختصة.",[("الرئيسية","index.html"),("خدمات المستثمرين",None)]) + f'''
<section class="s"><div class="wrap"><div class="grid g3">
<article class="card"><h3>تجهيز متطلبات التأسيس</h3><p>تنظيم بيانات الكيان والمستندات المطلوبة ومتابعة إجراءات التأسيس مع الجهات المختصة.</p></article>
<article class="card"><h3>التراخيص والمنصات</h3><p>متابعة التراخيص والتسجيل في المنصات الحكومية بحسب نوع النشاط.</p></article>
<article class="card"><h3>التشغيل والامتثال</h3><p>تنظيم التزامات المنشأة الدورية ومتابعة مواعيد التجديد.</p></article></div>
<p style="margin-top:24px">تُقدَّم الخدمات عبر القنوات الإلكترونية لجميع مناطق المملكة. للاطلاع على خدمات <a href="entity-misa.html">وزارة الاستثمار</a> و<a href="entity-business-center.html">المركز السعودي للأعمال</a> تفضل بزيارة صفحتيهما.</p></div></section>{cta()}'''
page("investors.html","خدمات المستثمرين","خدمات مساندة للمستثمرين ورواد الأعمال: تأسيس، تراخيص، منصات حكومية وتشغيل.",body,"services.html")

# ---------------- الأسئلة الشائعة
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in FAQ)
ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},ensure_ascii=False)
body = phero("الأسئلة الشائعة","إجابات مختصرة وواضحة عن آلية العمل والباقات والأتعاب.",[("الرئيسية","index.html"),("الأسئلة الشائعة",None)]) + f'<section class="s"><div class="wrap prose">{fq}</div></section><script type="application/ld+json">{ld}</script>{cta("لم تجد إجابة سؤالك؟","اسألنا مباشرة عبر واتساب.")}'
page("faq.html","الأسئلة الشائعة","الأسئلة الشائعة حول خدمات توضيح المعرفة: الطلب والمستندات والباقات والأتعاب والرسوم الحكومية.",body,"")

# ---------------- التواصل
mail = f'<li>البريد الإلكتروني: <a href="mailto:{C["email"]}">{C["email"]}</a></li>' if C["email"] else ""
body = phero("تواصل معنا وابدأ طلب خدمتك.","سواء كنت ترغب في تأسيس منشأة، أو متابعة إجراء حكومي، أو إدارة منصاتك، أو تأهيل شركتك للمشاريع، تواصل مع فريق توضيح المعرفة لمراجعة احتياجك.",[("الرئيسية","index.html"),("تواصل معنا",None)]) + f'''
<section class="s"><div class="wrap two"><div class="box"><h2>نموذج التواصل</h2>
<form id="cform" data-wa="{C['wa']}"><label for="name">الاسم</label><input id="name" name="name" required autocomplete="name">
<label for="company">اسم المنشأة</label><input id="company" name="company" autocomplete="organization">
<label for="type">نوع الاحتياج</label><select id="type" name="type"><option>تأسيس شركة أو مؤسسة</option><option>سجلات وتراخيص</option><option>إدارة المنصات الحكومية</option><option>موارد بشرية وموظفون</option><option>مشاريع ومنافسات</option><option>أخرى</option></select>
<label for="msg">تفاصيل طلبك</label><textarea id="msg" name="msg" rows="4"></textarea>
<p style="font-size:.9rem;color:var(--muted);margin-top:12px">عند الإرسال تُجهَّز رسالة واتساب جاهزة على جهازك لتراجعها وترسلها بنفسك. لا يحفظ الموقع بياناتك. لا ترسل أرقام هوية أو بيانات مالية في الرسالة الأولى.</p>
<button class="btn btn-p" type="submit">جهّز رسالة واتساب</button></form></div>
<aside><div class="box"><h2>قنوات التواصل</h2><ul style="list-style:none;padding:0"><li>واتساب بزنس: <a href="{wa()}" dir="ltr" target="_blank" rel="noopener">{C['phone_display']}</a></li><li>الهاتف: <a href="tel:{C['phone_tel']}" dir="ltr">{C['phone_display']}</a></li>{mail}</ul></div>
<div class="box"><h2>بيانات الشركة</h2><p><strong>المقر:</strong> {C['city']}</p><p><strong>نطاق الخدمة:</strong> جميع مناطق المملكة عبر القنوات الإلكترونية المتاحة.</p></div></aside></div></section>'''
page("contact.html","تواصل معنا","تواصل مع توضيح المعرفة لخدمات الأعمال عبر واتساب أو الهاتف لطلب خدمتك. المقر: حائل.",body,"contact.html")

# ---------------- القانونية (مسودات تحتاج مراجعة قانونية)
def legal(fn, title, secs):
    b = "".join(f"<h2>{h}</h2><p>{p}</p>" for h,p in secs)
    body = phero(title,"آخر تحديث: 10 نوفمبر 2026. مسودة تتطلب مراجعة قانونية قبل الاعتماد النهائي.",[("الرئيسية","index.html"),(title,None)]) + f'<section class="s"><div class="wrap prose box">{b}</div></section>'
    page(fn, title, f"{title} - توضيح المعرفة لخدمات الأعمال", body, "")
legal("privacy.html","سياسة الخصوصية",[("البيانات التي نجمعها","لا يحفظ هذا الموقع بياناتك. نموذج التواصل يجهّز رسالة واتساب على جهازك لترسلها بنفسك، وما تشاركه عبر واتساب يخضع لسياسة واتساب وللتواصل المباشر بينك وبيننا."),
 ("استخدام البيانات","نستخدم المعلومات التي ترسلها إلينا لمراجعة طلبك والرد عليك وتقديم الخدمة المتفق عليها فقط، ولا نبيعها لأي طرف."),
 ("الخطوط والخدمات الخارجية","يحمّل الموقع خط IBM Plex Sans Arabic من خدمة Google Fonts، وقد تتلقى هذه الخدمة عنوان IP الخاص بك عند تحميل الصفحة."),
 ("المستندات والبيانات الحساسة","لا ترسل كلمات مرور أو أرقام بطاقات أو بيانات مالية عبر الموقع. نطلب المستندات اللازمة عند بدء تنفيذ الخدمة وفق الاتفاق."),
 ("حقوقك","يمكنك طلب تصحيح بياناتك أو حذفها من سجلاتنا بالتواصل معنا عبر واتساب.")])
legal("terms.html","الشروط والأحكام",[("طبيعة الشركة","توضيح المعرفة جهة خاصة وليست جهة حكومية. نقدم خدمات مساندة لتجهيز الطلبات ومتابعتها، والقرار النهائي للجهة الحكومية المختصة."),
 ("لا ضمان للنتائج","لا نضمن موافقة أي جهة على أي طلب ولا ترسية أي منافسة."),
 ("المعلومات المنشورة","المعلومات في الموقع للتعريف العام، ونوثقها من المصادر الرسمية وقد تتغير. الرجوع للمصدر الرسمي للخدمة هو المعتمد."),
 ("الأتعاب والرسوم","تُحدد أتعاب الشركة كتابيًا قبل بدء الخدمة، وهي منفصلة عن الرسوم الحكومية التي تُسدَّد للجهة المختصة."),
 ("مسؤولية العميل","يلتزم العميل بصحة البيانات والمستندات التي يقدمها وبسريانها نظامًا.")])
legal("refund.html","سياسة الإلغاء والاسترجاع",[("الإلغاء قبل البدء","يمكن إلغاء الطلب قبل بدء التنفيذ بإشعارنا عبر واتساب."),
 ("بعد بدء التنفيذ","تُحتسب الأعمال المنجزة فعليًا حتى وقت الإلغاء وفق الاتفاق المكتوب للخدمة."),
 ("الرسوم الحكومية","الرسوم المسددة للجهات الحكومية تخضع لسياسات تلك الجهات في الإلغاء والاسترجاع، ولا تملك الشركة التحكم فيها."),
 ("الاتفاق المكتوب","تحدد تفاصيل الاسترجاع النهائية في عرض الخدمة المتفق عليه مع كل عميل.")])

# ---------------- ملفات مساندة
with open(os.path.join(OUT,"services.json"),"w",encoding="utf-8") as f:
    json.dump({"schema":["id","name","entity","platform","description","audience","requirements","documents","steps","outputs","source","reviewed","status"],"entities":[{"slug":e[0],"name":e[1],"category":e[4]} for e in ENTITIES],"services":SERVICES},f,ensure_ascii=False,indent=2)
base = C["base_url"]
with open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{base}{p}</loc></url>" for p in PAGES)+"</urlset>")
with open(os.path.join(OUT,"robots.txt"),"w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n")
open(os.path.join(OUT,".nojekyll"),"w").close()
print(len(PAGES),"pages")
