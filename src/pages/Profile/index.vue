<template>
  <main class="main container">
    <section class="main block">
      <div class="main__column first">
        <img class="main__user-icon user-icon"
             :src="defaultPicture"
             alt="defaultPicture"
        />
      </div>
      <div class="main__column second">
        <h6 class="main__title title">Информация</h6>
        <p class="main__information name">Имя Фамилия</p>
        <p class="main__information role">Должность</p>
      </div>
      <div class="main__column third"></div>
      <div class="main__column fourth">
        <button class="main__more-btn more-btn">Редактировать</button>
      </div>
    </section>
    <section class="tasks">
      <h3 class="tasks__title title">Задачи</h3>
      <div class="tasks__list left">
        <h7 class="tasks__list list-title">Оставшиеся</h7>
        <p class="tasks__name one">Оставшиеся</p>
        <p class="tasks__name one">Оставшиеся</p>
        <p class="tasks__name one">Оставшиеся</p>
      </div>
      <div class="tasks__list right">
        <h8 class="tasks__list list-title">В процессе</h8>
        <p class="tasks__name two">В процессе</p>
        <p class="tasks__name two">В процессе</p>
        <p class="tasks__name two">В процессе</p>
      </div>
    </section>
  </main>
</template>

<script>
import defaultPicture from "@/assets/images/user-icon.png";

export default {
  name: "ProfilePage",
  data: () => ({
    defaultPicture: defaultPicture,
  }),
}
</script>

<style scoped lang="scss">

.block {
  display: flex;
  flex-direction: row;
  padding-bottom: 10%;

  .first {
    width: 20%;
    align-items: flex-end;
  }

  .second {
    width: 25%;
    display: grid;
    grid-row-gap: 1px;
    grid-template-columns: 1fr 1fr;
    grid-template-areas:  "title title"
                          "name name"
                          "role role";
  }

  .name {
    grid-area: name;
  }

  .title {
    grid-area: title;
  }

  .role {
    grid-area: role;
  }

  .third {
    width: 25%;
  }

  .fourth {
    width: 25%;
  }

  .user-icon {
    width: 185px;
  }
}

.tasks {
  display: grid;
  grid-row-gap: 5px;
  grid-column-gap: 100px;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
      "title title"
      "left right";

  .left {
    grid-area: left;
    background: linear-gradient(95.68deg, #FF008A -16.11%, #8002FF 54.53%);
    border-radius: 10px;
    width: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
  }

  .right {
    grid-area: right;
    background: white;
    border-radius: 10px;
    width: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
  }

  .title {
    grid-area: title;
    margin-bottom: 3%;
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
</style>