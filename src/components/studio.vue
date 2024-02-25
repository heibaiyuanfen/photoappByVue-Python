<template>
    <div class="studio">
      <top-bar></top-bar> <!-- 假设你有一个顶部导航栏组件 -->
      <user-info></user-info> <!-- 用户信息组件 -->
     
      <image-wall></image-wall> <!-- 照片墙组件 -->
      <trial-bar></trial-bar> <!-- 试用栏组件 -->
      <bottom-nav-bar></bottom-nav-bar>
    </div>
  </template>
  
  <script>
  import TopBar from '@/components/TopBar.vue'
  import UserInfo from '@/components/UserInfo.vue';
  // import ImageWall from './ImageWall.vue';
  // import TrialBar from './TrialBar.vue';
  import BottomNavBar from '@/components/BottomNavBar.vue';
  
  export default {
    components: {
      TopBar,
      UserInfo,
      // ImageWall,
      // TrialBar,
      BottomNavBar
    }
  };
  </script>
  
  <style scoped>
  /* 在这里添加你的CSS样式 */
  .studio {
    display: flex;
    flex-direction: column;
  }
  /* 根据需要添加更多样式 */
  </style>
  