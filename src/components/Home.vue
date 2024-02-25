<template>
    <div class="home">
      <top-bar></top-bar> <!-- 假设你有一个顶部导航栏组件 -->
      <!-- 这里可以添加更多的 Home 页面特有的内容 -->
      <div class="content">
        <h1>Welcome to the Home Page</h1>
        <!-- 其他内容 -->
      </div>
      <bottom-nav-bar></bottom-nav-bar>
    </div>
  </template>
  
  <script>
  import TopBar from './TopBar.vue';
  import BottomNavBar from './BottomNavBar.vue';
  
  export default {
    components: {
      TopBar,
      BottomNavBar
    }
  };
  </script>
  
  <style scoped>
  /* 在这里添加你的CSS样式 */
  .home {
    display: flex;
    flex-direction: column;
  }
  .content {
    flex-grow: 1;
    /* 根据需要添加样式 */
  }
  </style>
  