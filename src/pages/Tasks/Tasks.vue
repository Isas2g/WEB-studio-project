<template>
  <main class="main">
  <h1 class="main__title title">Задачи</h1>
  <section class="main list">
    <div class="main__list all">
      <h8 class="main__list title">Все</h8>
      <p class="main__name two">Задача</p>
      <p class="main__name two">Задача</p>
      <p class="main__name two">Задача</p>
    </div>
    <div class="main__list active">
      <h7 class="main__list title">Активные</h7>
      <p class="main__name one">Задача</p>
      <p class="main__name one">Задача</p>
      <p class="main__name one">Задача</p>
    </div>
    <div class="main__list consider">
      <h7 class="main__list title">На рассмотрении</h7>
      <p class="main__name one">Задача</p>
      <p class="main__name one">Задача</p>
      <p class="main__name one">Задача</p>
    </div>
    <button v-on:click="showAlert" class="projects__arrow">
      <img :src="BtnArr" alt="BtnArr"/>
    </button>
    <button class="main__more-btn more-btn">Документы</button>
  </section>
    <section class="backlog">
      <h1 class="backlog__title title">Бэклог</h1>
      <p class="backlog__sprint sprint-title">Спринт 1</p>
      <div class="backlog__sprint first">
        <div class="backlog__sprint style-one"><p class="backlog_sprint task-first">текст текст текст</p></div>
        <div class="backlog__sprint style-two"><p class="backlog_sprint task-second">текст текст текст</p></div>
        <div class="backlog__sprint style-two"><p class="backlog_sprint task-second">текст текст текст</p></div>
        <div class="backlog__sprint style-one"><p class="backlog_sprint task-first">текст текст текст</p></div>
      </div>
      <p class="backlog__sprint sprint-title">Спринт 2</p>
      <div class="backlog__sprint first">
        <div class="backlog__sprint style-one"><p class="backlog_sprint task-first">текст текст текст</p></div>
        <div class="backlog__sprint style-two"><p class="backlog_sprint task-second">текст текст текст</p></div>
        <div class="backlog__sprint style-two"><p class="backlog_sprint task-second">текст текст текст</p></div>
        <div class="backlog__sprint style-one"><p class="backlog_sprint task-first">текст текст текст</p></div>
      </div>
    </section>
  </main>
</template>

<script>
import BtnArr from "@/assets/images/btn-strelka.png";

export default {
  name: "Tasks",
  data: () => ({
    BtnArr: BtnArr,
  }),
  methods: {
    showAlert: function () {
      alert("Эта часть сайта ещё в работе...");
    },
  },
}
</script>

<style scoped lang="scss">
.main {
  margin-left: 3%;
  margin-right: 1%;
}
.title {
  margin-bottom: 3%;
}
.list {
  display: grid;
  align-content: center;
  align-items: center;
  justify-content: center;
  justify-items: center;
  grid-row-gap: 5px;
  grid-column-gap: 3%;
  grid-template-columns: 10fr 10fr 10fr 0.5fr;
  grid-template-areas: "left center right arrow"
                        ". btn . .";
  .all {
    grid-area: left;
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 10px;
    padding: 5%;
    width: 90%;
  }
  .active {
    grid-area: center;
    display: flex;
    flex-direction: column;
    background: linear-gradient(95.68deg, #FF008A -16.11%, #8002FF 54.53%);
    border-radius: 10px;
    padding: 5%;
    width: 90%;
  }
  .consider {
    background: linear-gradient(95.68deg, #ff0000 -16.11%, #ff008a 54.53%);
    border-radius: 10px;
    padding: 5%;
    grid-area: right;
    display: flex;
    flex-direction: column;
    width: 90%;
  }

  .title {
    text-align: center;
  }

  .main__more-btn {
    grid-area: btn;
    width: 50%;
    margin-top: 20%;
    margin-left: 15%;
  }

  .projects__arrow {
    grid-area: arrow;
    background: none;
    border: none;
  }

  .one {
    font-size: 20px;
    font-style: normal;
    background-color: white;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    margin-top: 2%;
  }

  .two {
    font-size: 20px;
    font-style: normal;
    margin-top: 2%;
    background-color: black;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
  }
}

.backlog {

  .title {
    margin-top: 5%;
    margin-bottom: 5%;
  }

  .sprint-title {
    font-weight: bold;
  }

  .first {
    margin-left: 5%;
    margin-right: 7%;
    margin-bottom: 5%;
  }

  .style-one {
    background-color: white;
    border-radius: 5px;
    padding-left: 1%;
    height: 42px;
  }

  .style-two {
    background: linear-gradient(95.68deg, #ff0000 -16.11%, #ff008a 54.53%);
    border-radius: 5px;
    padding-left: 1%;
    height: 42px;
  }

  .task-second {
    font-size: 20px;
    font-style: normal;
    background-color: white;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    font-weight: bold;
  }

  .task-first {
    font-size: 20px;
    font-style: normal;
    background-color: black;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    font-weight: bold;
  }
}

@media (max-width: 1024px) {
  .main__more-btn {
    width: 100%;
    text-align: center;
    padding: 0;
  }
}
</style>