<template>
  <main class="main container">
    <section class="main block">
      <img class="main__user-icon user-icon" :src="defaultPicture" alt="defaultPicture" />
      <h4 class="main__title title">Информация</h4>
      <p class="main__information name">Имя</p>
      <p class="main__information surname">Фамилия</p>
      <p class="main__information role">Должность</p>
      <button class="main__more-btn more-btn">Редактировать</button>
    </section>
  </main>
</template>

<script>
import defaultPicture from "@/assets/images/user-icon.png";

export default {
  name: "Profile",
  data: () => ({
    defaultPicture: defaultPicture,
  }),
}
</script>

<style scoped lang="scss">
//.block {
//  display: grid;
//  grid-row-gap: 5px;
//  grid-column-gap: 1px;
//  grid-template-columns: 1fr 1fr 1fr 1fr;
//  grid-template-areas:
//      "user name surname btn"
//      "user role role ."
//      "user . ."
//}
//
//.main__information {
//  &__name {
//    grid-area: name;
//  }
//  &__surname {
//    grid-area: surname;
//  }
//  &__user-icon {
//    grid-area: user;
//  }
//  &__role {
//    grid-area: role;
//  }
//}
//
//.main__more-btn {
//  grid-area: btn;
//}
</style>