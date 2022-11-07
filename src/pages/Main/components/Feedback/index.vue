<template>
  <section class="feedback">
    <div class="feedback__body">
      <div class="feedback__first-column">
        <h1 class="feedback__title title">Отзывы</h1>
        <p class="feedback__subtitle subtitle">Почитайте отзывы...</p>
        <button class="feedback__more-btn more-btn">
          <router-link class="feedback__allFeedbackLink" to="/feedback"
            >Все отзывы</router-link
          >
        </button>
      </div>
      <div class="feedback__space"></div>
      <div class="feedback__second-column">
        <img class="feedback__user-icon" :src="UserIcon" alt="UserIcon" />
        <p class="feedback__text name">Александр</p>
        <p class="feedback__text text">
          Быстро и качественно сделали сайт! Рекомендую!
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import UserIcon from "@/assets/images/user-icon.png"

  export default {
    name: 'Feedback',
    data: () => ({
      UserIcon: UserIcon
    })
  }

</script>

<style scoped lang="scss">
  .feedback {
    &__body {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      margin-top: 30px;
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

  @media (max-width: 768px) {
    .feedback {
      &__body {
        margin-left: 34%;
        width: 250px;
        display: grid;
        justify-items: center;
        text-align: center;
        //flex-direction: column;
        grid-template-areas:
          "title"
          "sub"
          "user"
          "name"
          "text"
          "btn";
      }

      &__title {
        grid-area: title;
        font-size: 30px;
      }

      &__subtitle {
        grid-area: sub;
        margin-top: 31px;
        margin-bottom: 37px;
      }

      button.more-btn {
        grid-area: btn;
        width: 100%;
        margin-top: 105px;
        font-size: 16px;
        text-align: center;
        white-space: nowrap;
      }

      &__first-column {
        display: contents;
      }

      &__second-column {
        display: contents;
      }

      &__user-icon {
        max-width: 107px;
        grid-area: user;
      }

      &__text.text {
        grid-area: text;
      }

      &__text.name {
        grid-area: name;
      }
    }
  }

  @media (max-width: 425px) {
    .feedback {
      &__body {
        margin-left: 0;
        justify-content: center;
      }
    }
  }

  @media (max-width: 376px) {
    .feedback {
      &__body {
        padding: 0;
        margin: 0 0 0 25%;
        width: auto;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-areas:
          ". title ."
          ". sub ."
          ". user ."
          ". name ."
          ". text ."
          ". btn .";
      }

      &__title {
        grid-area: title;
        font-size: 30px;
      }

      &__subtitle {
        grid-area: sub;
        margin-top: 31px;
        margin-bottom: 37px;
      }

      button.more-btn {
        grid-area: btn;
        width: 100%;
        height: 37px;
        margin-top: 105px;
        font-size: 16px;
        text-align: center;
        white-space: nowrap;
      }

      &__first-column {
        display: contents;
      }

      &__second-column {
        display: contents;
      }

      &__user-icon {
        max-width: 107px;
        grid-area: user;
      }

      &__text.text {
        grid-area: text;
      }

      &__text.name {
        grid-area: name;
      }
    }
  }
</style>