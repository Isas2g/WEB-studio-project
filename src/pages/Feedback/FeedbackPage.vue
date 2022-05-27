<template>
  <div>
    <main class="feedback container">
      <section class="feedback__body">
        <h2 class="feedback__title">Отзывы</h2>
        <ul class="feedback__list">
          <Review
            name="Denis"
            text="Some text"
            stars="4"
            :image="defaultPicture"
          />
          <Review
            name="Aboba"
            text="Some text"
            stars="3"
            :image="defaultPicture"
          />
        </ul>
        <router-link class="feedback__to-main more-btn" to="/"
          >На главную</router-link
        >
      </section>
    </main>
  </div>
</template>


<script>
import Review from "./components/Review.vue";
import defaultPicture from "../../assets/images/user-icon.png";

export default {
  components: {
    Review,
  },
  data: () => ({
    defaultPicture: defaultPicture,
  }),
};
</script>

<style scoped lang="scss">
.feedback {
  &__to-main {
    display: block;
    margin: 50px auto 0 auto;
    width: fit-content;
  }
}
</style>