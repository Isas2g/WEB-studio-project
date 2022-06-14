<template>
  <div class="app">
    <Header />
    <router-view />
  </div>
</template>


<script>
import Header from "./components/Header.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style lang="scss">
@import url("./fonts.scss");
@import url("./breakpoints.scss");
img {
  pointer-events: none;
}

body {
  background-color: #000;
  color: #fff;
  font-family: "inter";
}
ul {
  list-style-type: none;
  margin-block-start: 0;
  margin-block-end: 0;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0 0 0 0;
}
h1 {
  background-image: linear-gradient(225deg, #f70193, #a72cf2);
  filter: drop-shadow(0 20px 30px #28d8ff33);
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-size: 40px;
  text-align: center;
}
h2 {
  background-image: linear-gradient(225deg, #f70193, #a72cf2);
  filter: drop-shadow(0 20px 30px #28d8ff33);
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-size: 40px;
  text-align: center;
}
h3 {
  background-image: linear-gradient(225deg, #f70193, #a72cf2);
  filter: drop-shadow(0 20px 30px #28d8ff33);
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-size: 35px;
  text-align: center;
}
h4 {
  font-size: 20px;

}
h5 {
  font-size: 16px;
  font-weight: 300;
}
h6 {
  background-image: linear-gradient(225deg, #f70193, #a72cf2);
  filter: drop-shadow(0 20px 30px #28d8ff33);
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-size: 35px;
  font-weight: bold;
}

h7 {
  font-size: 20px;
  background-color: white;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-weight: bold;
}

h8 {
  font-size: 20px;
  background-color: black;
  color: black;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  font-weight: bold;
}
p {
  font-size: 20px;
  font-style: normal;

}

a {
  text-decoration: none;
  color: inherit;
}
.container {
  max-width: 1200px;
  //padding: 40px 15px;
  margin: 0 auto;
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

@media (max-width: 1440px) {
  .container {
    max-width: 1000px;
  }
}

@media (max-width: 1024px) {
  button.more-btn {
    width: 250px;
    height: 45px;
    margin-top: 10px;
  }
}
</style>

