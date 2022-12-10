<template>
  <section class="task">
    <button class="task__button right">
      &#8592;
    </button>
    <p class="task__name">Задача</p>
    <button class="task__button left">
      &#8594;
    </button>
  </section>
</template>

<script>
export default {
  name: "Task",

}


</script>

<style lang="scss" scoped>

.task {
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  &__button {
    border: none;
    background: none;
  }
}

</style>