<template>
  <div class="container">
    <header>
      <div class="logo">
        Web-Studio
      </div>
      <ul>
        <li class="current">Главная</li>
        <li>Блог</li>
        <li>Хочу вступить!</li>
        <li>О нас</li>
        <li>Войти</li>
      </ul>
    </header>

    <main>
      <section class="main-block">
        <h1 class="title">Студенческая веб-студия Московского Политеха</h1>
        <p class="subtitle">Мы крутые ребята из Московского политеха и создаем крутой контент для тебя и всех остальных</p>
        <button class="more-btn">Подробнее</button>
      </section>
    </main>

  </div>
</template>

<script>
  export default {
    name: 'MainPage',
    // ...
  };
</script>

<style scoped lang="scss">

  .container {
    max-width: 1200px;
    padding: 40px 15px;
    margin: 0 auto;
    font-family: 'inter';
  }

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .logo {
      font-size: 18px;
    }

    .current {
      font-weight: 800;
    }

    ul {
      display: flex;
      list-style: none;

      li {
        margin-right: 15px;
        cursor: pointer;
      }
    }
  }

  .main-block {
    padding: 150px 0 150px 0;
  }
  
  .title {
    background-image: linear-gradient(225deg, #F70193, #A72CF2);
    filter: drop-shadow(0 20px 30px #28d8ff33);
    color: black;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    font-size: 50px;
    max-width: 670px;
    margin-bottom: 30px;
  }

  .subtitle {
    margin-bottom: 30px;
    max-width: 440px
  }

  .more-btn {
    background: linear-gradient(95.68deg, #FF0000 -16.11%, #FF008A 54.53%);
    border-radius: 5px;
    padding: 10px 50px;
    border: none;
    color: #fff;
    font-family: 'Inter';
    font-weight: 700;
    font-size: 16px;
  }

</style>