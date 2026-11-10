(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', o);
  });

  // بحث وتصفية الجهات والخدمات
  var q = document.getElementById('q'), f = document.getElementById('cat'), empty = document.getElementById('empty');
  function norm(s) { return (s || '').toLowerCase().replace(/[ً-ٟـ]/g, '').replace(/[أإآ]/g, 'ا').replace(/ة/g, 'ه').replace(/ى/g, 'ي'); }
  function run() {
    var t = norm(q ? q.value : ''), c = f ? f.value : '', shown = 0;
    document.querySelectorAll('[data-filter]').forEach(function (el) {
      var ok = (!t || norm(el.getAttribute('data-text')).indexOf(t) > -1) && (!c || el.getAttribute('data-cat') === c);
      el.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    if (empty) empty.style.display = shown ? 'none' : 'block';
  }
  if (q) q.addEventListener('input', run);
  if (f) f.addEventListener('change', run);

  // نموذج التواصل: يُجهّز رسالة واتساب دون إرسال أي بيانات إلى خوادم
  var form = document.getElementById('cform');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form), wa = form.getAttribute('data-wa');
    var msg = 'السلام عليكم، أرغب في التواصل مع توضيح المعرفة لخدمات الأعمال.\n' +
      'الاسم: ' + (d.get('name') || '') + '\nالمنشأة: ' + (d.get('company') || '') +
      '\nنوع الاحتياج: ' + (d.get('type') || '') + '\nالتفاصيل: ' + (d.get('msg') || '');
    window.open('https://wa.me/' + wa + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
})();
