<template>
    <div>
      <h2>测试后端通信</h2>
      <div v-if="images.length > 0">
        <h3>获取的图片列表：</h3>
        <ul>
          <li v-for="image in images" :key="image.id">
            <img :src="image.src" :alt="'Image ' + image.id" style="width: 100px;">
          </li>
        </ul>
      </div>
      <div v-else>
        <p>没有获取到图片。</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [],
      };
    },
    mounted() {
      this.fetchImages();
    },
    methods: {
      async fetchImages() {
        try {
          const response = await fetch('http://localhost:5000/api/images');
          if (!response.ok) throw new Error('Failed to fetch');
          const data = await response.json();
          console.log(data);
          this.images = data;
        } catch (error) {
          console.error("Error fetching images:", error);
        }
      },
    },
  };
  </script>
  