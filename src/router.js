import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/HoMe.vue'; // 主页组件
import Studio from './components/StuDio.vue'; // 工作室页组件

// 路由配置
const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/studio', component: Studio, name: 'Studio' },
  // 其他路由...
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
