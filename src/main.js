import { createApp } from 'vue';
import App from './App.vue'; // 引入根组件

// 如果你有路由文件(index.js)，它应该被命名为router.js，位于src文件夹下
import router from './router'; // 引入路由配置

// 创建Vue应用实例
const app = createApp(App);

// 使用路由
app.use(router);

// 挂载Vue应用实例到DOM
app.mount('#app');
