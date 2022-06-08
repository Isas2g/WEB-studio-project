<template>
  <main class="main container">
    <h1 class="main__title title">Задачи</h1>
    <section class="main list">
      <div class="main__list all">
        <h8 class="main__list title">Все</h8>
        <p2>Задача</p2>
        <p2>Задача</p2>
        <p2>Задача</p2>
      </div>
      <div class="main__list active">
        <h7 class="main__list title">Активные</h7>
        <p1>Задача</p1>
        <p1>Задача</p1>
        <p1>Задача</p1>
      </div>
      <div class="main__list consider">
        <h7 class="main__list title">На рассмотрении</h7>
        <p1>Задача</p1>
        <p1>Задача</p1>
        <p1>Задача</p1>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  name: "Tasks"
}
</script>

<style scoped lang="scss">
.title {
  margin-bottom: 3%;
}
.list {
  display: grid;
  grid-row-gap: 5px;
  grid-column-gap: 3%;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-areas: "left center right";
  .all {
    grid-area: left;
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 10px;
    padding: 5%;
  }
  .active {
    grid-area: center;
    display: flex;
    flex-direction: column;
    background: linear-gradient(95.68deg, #FF008A -16.11%, #8002FF 54.53%);
    border-radius: 10px;
    padding: 5%;
  }
  .consider {
    background: linear-gradient(95.68deg, #ff0000 -16.11%, #ff008a 54.53%);
    border-radius: 10px;
    padding: 5%;
    grid-area: right;
    display: flex;
    flex-direction: column;
  }

  .title {
    text-align: center;
  }

}
</style>