<template>
  <main class="join container">
    <section class="join__looking looking">
      <h2 class="looking__title">Кого мы ищем:</h2>
      <ul class="looking__persons">
        <li class="looking__person">
          <img
            class="looking__person-icon"
            src="../../assets/images/person-icon.svg"
            alt="Персона"
          />
          <div class="looking__person-info">
            <h4 class="looking__person-post">кого-то</h4>
            <h5 class="looking__person-skills">навыки</h5>
          </div>
        </li>
        <li class="looking__person">
          <img
            class="looking__person-icon"
            src="../../assets/images/person-icon.svg"
            alt="Персона"
          />
          <div class="looking__person-info">
            <h4 class="looking__person-post">кого-то</h4>
            <h5 class="looking__person-skills">навыки</h5>
          </div>
        </li>
        <li class="looking__person">
          <img
            class="looking__person-icon"
            src="../../assets/images/person-icon.svg"
            alt="Персона"
          />
          <div class="looking__person-info">
            <h4 class="looking__person-post">кого-то</h4>
            <h5 class="looking__person-skills">навыки</h5>
          </div>
        </li>
      </ul>
      <button class="looking__button more-btn" type="button">
        Подать заявку
      </button>
    </section>

    <section class="join-us">
      <h2 class="join-us__title">
        Хочешь к нам? Переходи по ссылке и заполняй форму!
      </h2>
      <a class="join-us__link" href="#">ссылка</a>
    </section>
  </main>
</template>


<script>
export default {
  components: {},
};
</script>

<style lang="scss">
.looking {
  &__title {
    margin-bottom: 20px;
  }

  &__persons {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  &__person {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
  &__person-info {
    margin: 0 0 0 30px;
  }
  &__button {
    display: block;
    margin: 100px auto 0 auto;
    cursor: pointer;
  }
}
.join-us {
  margin: 150px 0 0 0;
  &__link {
    display: block;
    text-align: center;
  }
}
</style>