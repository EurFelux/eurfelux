marked.use(markedKatex({
  throwOnError: true,
  nonStandard: true
}));

const renderer = new marked.Renderer();

renderer.heading = function (headingObj) {
  const headingId = headingObj.text.toLowerCase().replace(/ /g, '-');
  // 返回带有 id 的标题 HTML
  return `<h${headingObj.depth} id="${headingId}">
  <a href="#${headingObj.text}">${headingObj.text}</a>
  </h${headingObj.depth}>`;
};

marked.setOptions({
  renderer: renderer,
});
