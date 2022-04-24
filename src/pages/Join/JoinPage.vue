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
    </section>
  </main>
</template>


<script>
export default {
  components: {},
};
</script>

<style lang="scss">
.looking__persons {
  display: flex;
}
</style>