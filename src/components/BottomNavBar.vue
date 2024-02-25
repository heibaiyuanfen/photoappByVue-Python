<template>
    <div class="bottom-nav-bar">
      <button class="nav-item" @click="goTo('home')">Home</button>
      <button class="nav-item" @click="goTo('studio')">Studio</button>
      <!-- 根据需要添加更多按钮 -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'BottomNavBar',
    methods: {
      goTo(screenName) {
        // 触发事件，让父组件处理页面跳转
        this.$emit('navigate', screenName);
      },
    },
  };
  </script>
  
  <style scoped>
  .bottom-nav-bar {
    display: flex;
    justify-content: space-around;
    background-color: #f8f8f8;
    padding: 0.5rem 0;
  }
  
  .nav-item {
    background: none;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
  }
  </style>
  