<template>
  <div class="app">
    <Header />
    <router-view />
  </div>
</template>


<script>
import Header from "./components/Header/Header.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style lang="scss">
@import url("./fonts.scss");

.container {
  max-width: 1200px;
  padding: 40px 15px;
  margin: 0 auto;
  font-family: "inter";
}

.title {
  background-image: linear-gradient(225deg, #f70193, #a72cf2);
  filter: drop-shadow(0 20px 30px #28d8ff33);
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-size: 50px;
  max-width: 670px;
  margin-bottom: 30px;
}

.subtitle {
  margin-bottom: 30px;
  max-width: 440px;
}

.more-btn {
  background: linear-gradient(95.68deg, #ff0000 -16.11%, #ff008a 54.53%);
  border-radius: 5px;
  padding: 10px 50px;
  border: none;
  color: #fff;
  font-family: "Inter";
  font-weight: 700;
  font-size: 16px;
}
</style>

