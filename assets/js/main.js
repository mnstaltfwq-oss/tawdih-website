(() => {
  const phone = '966535448100';
  const wa = (service, agency = 'عام') => `https://wa.me/${phone}?text=${encodeURIComponent(`مرحباً، أرغب بالاستفسار عن ${service}${agency !== 'عام' ? ` لدى ${agency}` : ''}.`)}`;
  const esc = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
  const categories = [
    { id: 'setup', title: 'تأسيس المنشآت', icon: '◇', text: 'ابدأ منشأتك بخطوات مرتبة من اختيار الكيان إلى استكمال المتطلبات.' },
    { id: 'licenses', title: 'التراخيص', icon: '▤', text: 'مساندة في متابعة الرخص والتصاريح وتجديدها حسب نشاطك.' },
    { id: 'employees', title: 'شؤون الموظفين', icon: '♧', text: 'تنظيم إجراءات الموظفين والعقود والخدمات المرتبطة بالعمل.' },
    { id: 'payroll', title: 'الرواتب', icon: '▦', text: 'دعم إداري في تنظيم ملفات الرواتب ومتابعة متطلباتها.' },
    { id: 'insurance', title: 'التأمينات', icon: '＋', text: 'متابعة خدمات الاشتراك وتحديث بيانات المنشأة والمشتركين.' },
    { id: 'tax', title: 'الزكاة والضرائب', icon: '٪', text: 'مساندة في تنظيم المتطلبات ومتابعة الإجراءات ذات العلاقة.' }
  ];
  const agencies = [
    { id: 'qiwa', title: 'قوى', icon: 'ق', desc: 'خدمات العمل للمنشآت', tags: 'موظفين عمل عقود نقل خدمات' },
    { id: 'gosi', title: 'التأمينات الاجتماعية', icon: 'ت', desc: 'شؤون المشتركين والاشتراكات', tags: 'تأمينات موظفين اشتراك أجور' },
    { id: 'commerce', title: 'وزارة التجارة', icon: 'م', desc: 'السجلات والكيانات التجارية', tags: 'تأسيس سجل تجاري شركات' },
    { id: 'absher-muqeem', title: 'أبشر أعمال ومقيم', icon: 'أ', desc: 'خدمات المنشآت والمقيمين', tags: 'موظفين إقامة جوازات مقيم' },
    { id: 'zatca', title: 'هيئة الزكاة والضريبة والجمارك', icon: 'ز', desc: 'متطلبات الزكاة والضرائب', tags: 'زكاة ضريبة فواتير' },
    { id: 'balady', title: 'بلدي وسلامة', icon: 'ب', desc: 'الرخص البلدية والتصاريح', tags: 'تراخيص رخص بلدية سلامة' }
  ];
  const faq = {
    qiwa: ['ما الخدمات التي يمكن متابعتها عبر قوى؟|نساعد في فهم متطلبات خدمات المنشآت مثل ملفات العمل والعقود والخدمات المرتبطة بالموظفين.', 'هل يمكنكم متابعة نقل خدمات الموظفين؟|نوضح المتطلبات ونساند في متابعة الإجراء وفق صلاحيات المنشأة وحالة الطلب.', 'ما الذي أجهزه قبل طلب الخدمة؟|جهّز بيانات المنشأة والموظف وأي معلومات أو مستندات تظهر ضمن متطلبات الخدمة.', 'هل تضمنون قبول الطلب؟|لا؛ القرار للجهة المختصة. دورنا المساندة الإدارية والمتابعة والتوضيح.'],
    gosi: ['ما خدمات التأمينات التي تقدمون بشأنها مساندة؟|متابعة إجراءات المنشأة والمشتركين وتوضيح الخطوات والمتطلبات المتاحة.', 'كيف أتابع تسجيل مشترك؟|نراجع معك المعلومات المطلوبة ونرشدك إلى خطوات الإجراء عبر القنوات الرسمية.', 'هل تساعدون في تحديث بيانات الأجور؟|نساند في ترتيب البيانات ومتابعة الإجراء وفق المتطلبات المعروضة في حساب المنشأة.', 'ما المستندات المطلوبة؟|تختلف حسب الإجراء؛ نحددها معك بعد معرفة الحالة ونوع الطلب.'],
    commerce: ['هل تساعدون في تأسيس سجل تجاري؟|نوضح خطوات التأسيس والمتطلبات ونساندك في متابعة الطلب عبر القنوات الرسمية.', 'ما المعلومات اللازمة لبدء التأسيس؟|عادةً نبدأ بالنشاط والكيان المقترح وبيانات المالكين، ثم نحدد المتطلبات بحسب الحالة.', 'هل يمكن متابعة تعديل بيانات السجل؟|نعم، يمكننا توضيح خطوات التعديل ومساندة المنشأة في متابعة الطلب.', 'هل أنتم جهة حكومية؟|لا، نحن شركة خاصة لخدمات الأعمال ولا نمثل وزارة التجارة أو أي جهة حكومية.'],
    'absher-muqeem': ['ما الفرق بين أبشر أعمال ومقيم؟|هما منصتان لخدمات مختلفة للمنشآت؛ نساعدك في تحديد المسار المناسب حسب الإجراء.', 'هل تساعدون في إجراءات الإقامة؟|نساند في فهم المتطلبات ومتابعة الإجراء المتاح وفق صلاحية المنشأة.', 'ما البيانات التي أجهزها؟|جهّز بيانات المنشأة والمقيم ورقم الطلب أو تفاصيل الحالة إن وجدت.', 'هل يمكنكم ضمان إنجاز المعاملة؟|لا نضمن قرارات الجهات أو أوقات معالجتها؛ نقدم مساندة ومتابعة واضحة.'],
    zatca: ['ما نوع الخدمات التي تساندون فيها؟|توضيح ومساندة إدارية في الإجراءات المرتبطة بمتطلبات الزكاة والضرائب.', 'هل تقدمون استشارات ضريبية؟|نقدم خدمات مساندة إدارية، ولا تحل محل الاستشارة الضريبية المهنية المتخصصة.', 'كيف أبدأ استفساراً عن الفوترة الإلكترونية؟|أرسل وصف احتياج منشأتك عبر واتساب لنوضح نطاق المساندة والمتطلبات الأولية.', 'هل تمثلون هيئة الزكاة والضريبة والجمارك؟|لا؛ توضيح المعرفة شركة خاصة مستقلة ولا تمثل الهيئة.'],
    balady: ['هل تساعدون في استخراج رخصة بلدية؟|نوضح الخطوات ونساند في متابعة طلبات الرخص بحسب النشاط والموقع.', 'هل تشمل المساندة متطلبات السلامة؟|نساعد في فهم المتطلبات والإجراءات ذات العلاقة، وفق نوع النشاط وحالته.', 'ما المعلومات المطلوبة لطلب رخصة؟|تختلف بحسب النشاط والموقع؛ شاركنا بيانات المنشأة لنحدد لك ما يلزم.', 'هل تضمنون الموافقة على الرخصة؟|لا؛ الموافقة تصدر من الجهة المختصة. نساند في تنظيم ومتابعة الإجراء فقط.']
  };
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#primary-nav');
  if (menuButton && navigation) {
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!open));
      menuButton.setAttribute('aria-label', open ? 'فتح القائمة' : 'إغلاق القائمة');
      navigation.classList.toggle('is-open', !open);
    });
    navigation.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
      menuButton.setAttribute('aria-expanded', 'false'); menuButton.setAttribute('aria-label', 'فتح القائمة'); navigation.classList.remove('is-open');
    }));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && navigation.classList.contains('is-open')) { menuButton.setAttribute('aria-expanded', 'false'); navigation.classList.remove('is-open'); menuButton.focus(); }
    });
  }
  document.querySelectorAll('a[data-service][data-agency]').forEach((link) => {
    link.href = wa(link.dataset.service, link.dataset.agency); link.target = '_blank'; link.rel = 'noopener noreferrer';
  });
  const year = document.querySelector('#current-year'); if (year) year.textContent = new Date().getFullYear();
  const page = document.body.dataset.page;
  if (page === 'home') {
    if (!document.querySelector('link[data-enhancements]')) { const style = document.createElement('link'); style.rel = 'stylesheet'; style.href = 'assets/css/enhancements.css'; style.dataset.enhancements = ''; document.head.append(style); }
    const hero = document.querySelector('.hero');
    if (hero && !document.querySelector('#service-finder')) {
      const finder = document.createElement('section'); finder.className = 'finder-section'; finder.id = 'service-finder'; finder.setAttribute('aria-labelledby', 'finder-heading');
      finder.innerHTML = `<div class="container"><div class="finder-intro"><span class="eyebrow">مساعدك لاختيار الخدمة</span><h2 class="section-title" id="finder-heading">ما الذي تحتاجه منشأتك؟</h2><p>اختر المجال الأقرب لاحتياجك، ونرشدك إلى الخدمات المناسبة.</p></div><div class="category-grid">${categories.map((item) => `<a class="category-card" href="services.html?category=${item.id}"><span class="category-icon" aria-hidden="true">${item.icon}</span><b>${item.title}</b><small>${item.text}</small><span class="category-arrow" aria-hidden="true">←</span></a>`).join('')}</div><a class="text-link" href="services.html">استعرض دليل الخدمات الكامل <span>←</span></a></div></section>`;
      hero.after(finder);
    }
    const directory = document.querySelector('#agencies .agency-grid');
    if (directory && !document.querySelector('#agency-search')) {
      const tools = document.createElement('div'); tools.className = 'directory-tools'; tools.innerHTML = '<label class="search-box"><span aria-hidden="true">⌕</span><span class="visually-hidden">ابحث عن جهة أو خدمة</span><input id="agency-search" type="search" placeholder="ابحث عن جهة أو خدمة…" autocomplete="off"></label><p class="search-count" aria-live="polite"></p>';
      directory.before(tools);
      const input = tools.querySelector('input'); const count = tools.querySelector('.search-count'); const cards = [...directory.querySelectorAll('.agency-card')];
      const filter = () => { const term = input.value.trim().toLocaleLowerCase('ar'); let shown = 0; cards.forEach((card) => { const visible = card.textContent.toLocaleLowerCase('ar').includes(term); card.hidden = !visible; if (visible) shown++; }); count.textContent = term ? `النتائج: ${shown}` : 'اختر جهة لاستعراض الخدمات المرتبطة بها'; };
      input.addEventListener('input', filter); filter();
    }
  }
  if (page === 'services') {
    const search = document.querySelector('#service-search'); const cards = [...document.querySelectorAll('.agency-directory-card')];
    const filters = [...document.querySelectorAll('[data-category-filter]')]; let activeCategory = new URLSearchParams(location.search).get('category') || 'all';
    const update = () => { const term = search.value.trim().toLocaleLowerCase('ar'); let visible = 0; cards.forEach((card) => { const textMatch = card.textContent.toLocaleLowerCase('ar').includes(term) || card.dataset.tags.includes(term); const categoryMatch = activeCategory === 'all' || card.dataset.categories.split(' ').includes(activeCategory); card.hidden = !(textMatch && categoryMatch); if (!card.hidden) visible++; }); document.querySelector('#directory-count').textContent = `يعرض ${visible} من ${cards.length} جهات`; };
    filters.forEach((button) => button.addEventListener('click', () => { activeCategory = button.dataset.categoryFilter; filters.forEach((item) => item.setAttribute('aria-pressed', String(item === button))); update(); }));
    search.addEventListener('input', update); filters.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.categoryFilter === activeCategory))); update();
  }
  if (page === 'agency') {
    const agencyId = new URLSearchParams(location.search).get('agency'); const agency = agencies.find((item) => item.id === agencyId) || agencies[0];
    const title = document.querySelector('#agency-title'); title.textContent = agency.title; document.querySelector('#agency-desc').textContent = agency.desc;
    document.title = `${agency.title} | دليل الجهات — توضيح المعرفة`;
    const serviceMap = {
      qiwa: ['إدارة ملفات المنشأة','العقود الوظيفية','متابعة خدمات الموظفين','توضيح متطلبات خدمات العمل'], gosi: ['تسجيل وتحديث بيانات المشتركين','متابعة الاشتراكات','تحديث بيانات الأجور','استفسارات خدمات التأمينات'], commerce: ['تأسيس الكيانات التجارية','إصدار وتجديد السجل التجاري','تعديل بيانات السجل','متابعة خدمات الشركات'], 'absher-muqeem': ['خدمات المنشآت والمقيمين','متابعة إجراءات الإقامة','تحديث بيانات العاملين','مساندة في خدمات مقيم'], zatca: ['متطلبات الزكاة','خدمات ضريبة القيمة المضافة','الفوترة الإلكترونية','متابعة الإجراءات والطلبات'], balady: ['إصدار وتجديد الرخص البلدية','متطلبات تراخيص الأنشطة','إجراءات السلامة','متابعة الطلبات البلدية']
    };
    const services = serviceMap[agency.id] || serviceMap.qiwa;
    document.querySelector('#agency-services').innerHTML = services.map((service) => `<article class="service-tile"><span class="tile-check" aria-hidden="true">✓</span><h3>${service}</h3><p>مساندة إدارية ومتابعة للخطوات والمتطلبات حسب حالة منشأتك.</p><a class="text-link" href="service.html?name=${encodeURIComponent(service)}&agency=${agency.id}">تفاصيل الخدمة <span>←</span></a></article>`).join('');
    document.querySelector('#agency-faq').innerHTML = (faq[agency.id] || faq.qiwa).map((entry) => { const [question, answer] = entry.split('|'); return `<details class="faq-item"><summary>${question}</summary><p>${answer}</p></details>`; }).join('');
    const request = document.querySelector('#agency-request'); request.href = wa('استفسار عن الخدمات', agency.title); request.target = '_blank'; request.rel = 'noopener noreferrer';
  }
  if (page === 'service') {
    const params = new URLSearchParams(location.search); const name = params.get('name') || 'خدمة الأعمال'; const agency = agencies.find((item) => item.id === params.get('agency')) || agencies[0];
    document.title = `${name} | توضيح المعرفة لخدمات الأعمال`; document.querySelector('#service-title').textContent = name; document.querySelector('#service-agency').textContent = agency.title;
    document.querySelector('#service-wa').href = wa(name, agency.title); document.querySelector('#service-wa').target = '_blank'; document.querySelector('#service-wa').rel = 'noopener noreferrer';
  }
})();
