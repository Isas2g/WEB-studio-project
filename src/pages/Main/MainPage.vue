<template>
  <div class="container">
    <main class="main">
      <section class="main__block">
        <h1 class="main__title title">
          Студенческая веб-студия Московского Политеха
        </h1>
        <p class="main__subtitle subtitle">
          Мы крутые ребята из Московского политеха и создаем крутой контент для
          тебя и всех остальных
        </p>
        <button class="main__more-btn more-btn">Подробнее</button>
      </section>
    </main>
    <carousel-team/>
    <projects class="projects">
      <container class="projects__container">
        <section class="projects__body">
          <h1 class="projects__title">Наши проекты</h1>
          <div class="projects__image-container">
            <img
                class="projects__image"
                :src="SmoothieFeed"
                alt="SmoothieFeed"
            />
            <button v-on:click="showAlert" class="projects__arrow">
              <img
                :src="BtnArr"
                alt="BtnArr"
              />
            </button>
          </div>
          <h3 class="projects__project-title">SmoothieFeed</h3>
          <a href="http://pd-2021-2.std-1376.ist.mospolytech.ru" target="__blank" class="projects__button more-btn">Подробнее</a>
        </section>
      </container>
    </projects>
    <feedback class="feedback">
      <section class="feedback__body">
        <section class="feedback__first-column">
          <h1 class="feedback__title title">Отзывы</h1>
          <p class="feedback__subtitle subtitle">Почитайте отзывы...</p>
          <button class="feedback__more-btn more-btn"><router-link class="feedback__allFeedbackLink" to="/feedback">Все отзывы</router-link></button>
        </section>
        <section class="feedback__space"></section>
        <section class="feedback__second-column">
          <img
              class="feedback__user-icon"
              :src="UserIcon"
              alt="UserIcon"
          />
          <p class="feedback__text name">Александр</p>
          <p class="feedback__text text">Быстро и качественно сделали сайт! Рекомендую!</p>
        </section>
      </section>
    </feedback>
    <footer class="footer">
      <section class="footer__body">
        <h1 class="footer__title title">Связаться с нами</h1>
        <p class="footer__subtitle subtitle">
          Оставьте свои контакты и мы свяжемся с вами в ближайшее время
        </p>
        <form class="footer__form" id="form">
          <input
            class="form__input name"
            type="text"
            id="name"
            name="name"
            placeholder="ИМЯ"
          />
          <input
            class="form__input phone"
            type="text"
            id="phone"
            name="phone"
            placeholder="ТЕЛЕФОН"
          />
          <input
            class="form__input email"
            type="text"
            id="email"
            name="email"
            placeholder="EMAIL"
          />
          <input
            class="form__input com"
            type="text"
            id="com"
            name="com"
            placeholder="КОММЕНТАРИЙ"
          />
        </form>
        <button class="footer__more-btn more-btn" form="form">Связаться</button>
      </section>
    </footer>
  </div>
</template>

<script>
import SmoothieFeed from "@/assets/images/smoothie-feed.jpg";
import UserIcon from "@/assets/images/user-icon.png";
import BtnArr from "@/assets/images/btn-strelka.png";
import CarouselTeam from "@/components/CarouselTeam";

export default {
  components: {CarouselTeam},
  data: () => ({
    SmoothieFeed: SmoothieFeed,
    UserIcon: UserIcon,
    BtnArr: BtnArr,
  }),
  methods: {
    showAlert: function() {
      alert('Эта часть сайта ещё в работе...');
    }
  }
};

</script>

<style lang="scss">
.main {
  &__block {
    max-width: 800px;
    padding: 0 0 150px 0; //зачем паддинг был 150 пикселей сверху?
  }
  &__title {
    text-align: start;
    margin-bottom: 20px;
  }
  &__subtitle {
    max-width: 440px;
    margin-bottom: 73px;
  }
}

.projects {
  &__container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    max-width: 480px;
    margin-left: 35%;
  }
  &__body {
    display: flex;
    flex-direction: column;
    padding-bottom: 330px;
    align-items: center;
  }
  &__arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 80%;
  }

  &__title {
    margin-bottom: 20px;
  }

  &__project-title {
    color: white;
    font-size: 35px;
  }

  &__image {
    max-width: 311px;
    border-radius: 30px;
    max-height: 365px;
    margin-bottom: 30px;
  }

  &__button {
    display: block;
    margin-top: 50px;
  }

  .projects__image-container {
    position: relative;
  }

  button.projects__arrow {
    position: absolute;
    right: -110px;
    top: 116px;
    bottom: 0;
    border: none;
    background: none;
    outline: none;
    margin: auto;
    height: 64px;
  }
}

.feedback {
  &__body {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 150px 330px 150px;
  }

  .name {
    font-weight: bold;
  }

  &__first-column {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  &__second-column {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 300px;
    align-items: center;
  }

  &__user-icon {
    max-width: 146px;
  }

  &__subtitle {
    margin-top: 20px;
    margin-bottom: 125px;
  }

  &__more-btn {
    margin-bottom: 5px;
  }
}

.footer {
  &__body {
    color: white;
    align-content: end;
    justify-content: center;
    padding: 0 150px 0 150px;
    text-align: center;
  }

  &__subtitle {
    text-align: center;
  }

  &__title {
    text-align: center;
  }

  &__form {
    padding-top: 78px;
    padding-bottom: 89px;
    display: grid;
    grid-row-gap: 60px;
    grid-column-gap: 80px;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas:
      "name phone email"
      "com com com";
  }
  .form__input {
    width: 100%;
  }
  .name {
    grid-area: name;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .phone {
    grid-area: phone;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .email {
    grid-area: email;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .com {
    grid-area: com;
    width: 100%;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
}
</style>