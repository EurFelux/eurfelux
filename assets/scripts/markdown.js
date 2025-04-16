// 设置 markdown 渲染器
marked.use(
  markedKatex({
    throwOnError: true,
    nonStandard: true,
  })
);

const renderer = new marked.Renderer();

renderer.heading = function (headingObj) {
  const headingId = headingObj.text.toLowerCase().replace(/ /g, "-");
  // 返回带有 id 的标题 HTML
  return `<h${headingObj.depth} id="${headingId}">
  <a href="#${headingObj.text}">${headingObj.text}</a>
  </h${headingObj.depth}>`;
};

marked.setOptions({
  renderer: renderer,
});

// 目录生成
function generateToc(markdownContents) {
  const headings = markdownContents.querySelectorAll("h1, h2, h3, h4, h5, h6");
  const nav = document.querySelector(".aside-nav");

  // 生成目录HTML
  const tocHtml = Array.from(headings)
    .map((heading) => {
      const level = parseInt(heading.tagName.charAt(1));
      const text = heading.textContent;
      const id = heading.id;

      return `<a href="#${id}" class="toc-item level-${level}">${text}</a>`;
    })
    .join("\n");

  nav.innerHTML = tocHtml;
}

/**
 * 初始化标题观察器，用于高亮当前可见标题对应的侧边栏链接
 */
function initHeadingObserver() {
  // 获取所有标题和侧边栏链接
  const headings = document.querySelectorAll('.markdown-contents h2, .markdown-contents h3, .markdown-contents h4');
  const sidebarLinks = document.querySelectorAll('aside nav a');

  // 创建 Intersection Observer 实例
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // 获取当前可见标题的ID
          const id = entry.target.id;
          const activeLink = document.querySelector(`.aside-nav a[href="#${id}"]`);
          // console.log(activeLink)

          // 更新侧边栏链接高亮状态
          if (activeLink) {
            sidebarLinks.forEach((link) => link.classList.remove('active'));
            activeLink.classList.add('active');
          }
        }
      });
    },
    {
      root: document.querySelector('body'),
      threshold: 0.5,
      rootMargin: '0px 0px -80% 0px',
    }
  );

  // 开始观察所有标题
  headings.forEach((heading) => observer.observe(heading));
}
