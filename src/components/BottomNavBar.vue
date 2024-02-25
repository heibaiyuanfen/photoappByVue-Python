<template>
    <div class="bottom-nav-bar">
      <button class="nav-item" @click="goTo('Home')">Home</button>
      <button class="nav-item" @click="goTo('Studio')">Studio</button>
      <!-- 根据需要添加更多按钮 -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'BottomNavBar',
    methods: {
      goTo(screenName) {
        // 触发事件，让父组件处理页面跳转
        this.$router.push({ name: screenName });
      },
    },
  };
  </script>
  
  <style scoped>
.bottom-nav-bar {
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff; /* 设置背景色 */
  box-shadow: 0 -2px 5px rgba(0,0,0,0.1); /* 可选：添加阴影效果 */
  z-index: 1000; /* 确保导航栏在其他内容之上 */
}
.content {
  padding-bottom: 60px; /* 底部导航栏的高度加上一些额外空间 */
}

  
  .nav-item {
    background: none;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
  }
  </style>
  