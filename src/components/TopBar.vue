<template>
    <div class="top-bar">
      <!-- Logo 或者标题 -->
      <div class="logo">
        <h1>MyApp</h1>
      </div>
      <!-- 右侧内容，比如时间、状态图标等 -->
      <div class="status-icons">
        <span class="time">23:38</span>
        <!-- 使用图标库或图片 -->
        <i class="fas fa-bell"></i> <!-- 假设使用Font Awesome -->
        <i class="fas fa-wifi"></i>
        <i class="fas fa-battery-full"></i>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TopBar',
    // 这里可以添加 props, data, methods 等选项
  };
  </script>
  
  <style scoped>
  .top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #333;
    color: #fff;
  }
  
  .logo h1 {
    margin: 0;
  }
  
  .status-icons {
    display: flex;
    align-items: center;
    font-size: 1.2rem;
  }
  
  .status-icons i {
    margin-left: 10px;
  }
  </style>
  