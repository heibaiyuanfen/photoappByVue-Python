<template>
    <div class="user-info">
      <img class="avatar" src="path/to/avatar.png" alt="User avatar" />
      <div class="user-details">
        <h2 class="username">Username</h2>
        <!-- 其他用户相关信息 -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserInfo',
    // 在这里可以添加 props, data, methods 等选项
  };
  </script>
  
  <style scoped>
  .user-info {
    display: flex;
    align-items: center;
    padding: 1rem;
  }
  
  .avatar {
    width: 60px; /* 根据实际需要调整 */
    height: 60px; /* 根据实际需要调整 */
    border-radius: 50%; /* 使图片呈圆形 */
    margin-right: 1rem;
  }
  
  .username {
    font-size: 1.2rem;
    margin: 0;
  }
  </style>
  