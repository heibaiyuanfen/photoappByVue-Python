<!-- Home.vue -->
<template>
  <div class="home">
    <!-- Top bar with icons and title -->
    <div class="top-bar">
      <span class="time">23:38</span>
      <div class="icons">
        <!-- Icons here (use svg or icon library) -->
        <span>🔔</span> <!-- Example emoji icon -->
      </div>
    </div>

    <!-- User info section -->
    <user-info></user-info>

    <top-bar></top-bar>
    <test-api></test-api>

    <!-- 路由视图：用于展示基于路由的组件 -->
    <router-view></router-view>

    <!-- Image wall/grid -->
    <div class="image-wall">
      <div class="image-item" v-for="image in images" :key="image.id">
        <img :src="image.src" alt="User content"/>
      </div>
    </div>

    
    <!-- Trial bar -->
    <div class="trial-bar">
      <p>Tap here to unlock 7 days of VSCO Membership for free.</p>
      <button class="trial-button">Try for free</button>
    </div>

    <!-- Bottom navigation bar -->
    <bottom-nav-bar></bottom-nav-bar>
  </div>
</template>

<script>
import UserInfo from './components/UserInfo.vue';
import BottomNavBar from './components/BottomNavBar.vue'
import TopBar from './components/TopBar.vue';
import TestApi from './components/TsetApi.vue';

export default {
  components: {
    UserInfo,
    BottomNavBar,
    TopBar,
    TestApi
  },
  data() {
    return {
      images: [
        // Fill with your image data
      ]
    }
  }
}
</script>

<style scoped>
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}
.user-info {
  /* Styles for user info */
}
.image-wall {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}
.image-item img {
  width: 100%;
  height: auto;
  display: block;
}
.trial-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #f3f3f3;
}
.trial-button {
  padding: 0.5rem 1rem;
  background-color: blue;
  color: white;
  border: none;
  border-radius: 0.5rem;
}
.bottom-nav-bar {
  /* Styles for bottom nav bar */
}
</style>
