<template>
    <div v-if="show" class="background" >
      <div class="hystmodal_wrap">
        <div class="modal">
          <form
              class="modalBodyWrapper"
              @submit="sendForm"
          >
            <slot name="title">
              <div class="modal-block-title">
                <h3 class="modal-title">Добавить задачу</h3>
                <div class="modal-close" @click="closeModal">&#10006;</div>
              </div>
            </slot>
            <slot name="body">
              <div class="modal-content">
                <form class="modal__form" id="form">
                  <input
                      class="form__input name"
                      type="text"
                      id="name"
                      name="name"
                      placeholder="Задача"
                  />
                  <input
                      class="form__input description"
                      type="text"
                      id="description"
                      name="description"
                      placeholder="Описание задачи"
                  />
                  <input
                      class="form__input comment"
                      type="text"
                      id="comment"
                      name="comment"
                      placeholder="Комментарий"
                  />
                </form>
                <div class="task__sort sort">
                  <p class="sort__text">Исполнитель</p>
                  <div class="sort__dropdown dropdown" @click="showUsers(shows)">
                    <p class="sort__dropdown-title">
                      {{ chosenUser }}
                    </p>
                    <img class="dropdown__image" :src="require('../../../assets/images/icons/iconBtnDown2.svg')"/>
                    <ul v-if="shows === true" class="dropdown__list is-show">
                      <li v-for="(item, index) in executor" :key="index" class="dropdown__item" @click="chooseUser(index)">
                        {{ item }}
                      </li>
                    </ul>
                    <ul v-else class="dropdown__list">
                      <li v-for="(item, index) in executor" :key="index" class="dropdown__item">
                        {{ item }}
                      </li>
                    </ul>
                  </div>
                </div>
                <button class="modal__add-user">&#43; Добавить исполнителя</button>
              </div>
            </slot>
            <slot name="footer">
              <div class="modal-footer">
                <button class="modal-footer_button" @click="closeModal">
                  Назад
                </button>
                <button class="modal-footer_button">
                  Сохранить
                </button>
              </div>
            </slot>
          </form>

        </div>
      </div>
    </div>

  </template>


<script>
export default {
  name: "TaskAdding",
  props:{
  },
  data: function () {
    return {
      show: false,
      shows: false,
      executor: [
        "Пользователь один",
        "Пользователь два",
        "Пользователь три",
        "Пользователь четыре",
      ],
      chosenUser: "Выберите исполнителя",
    }
  },
  computed: {},
  methods: {
    closeModal(){
      this.show = false;
    },
    async sendForm(e) {
      e.preventDefault()
    },
    showUsers(shows) {
      if (shows) {
        this.shows = false;
      } else {
        this.shows = true;
      }
    },
    chooseUser(index) {
      this.chosenUser = this.executor[index];
    }
  },
  mounted(){
  },
  created() {

  }
}
</script>

<style scoped>
.background {
  z-index: 10;
  position: fixed;
  overflow: auto;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.85);
}

.modal{
  border-radius: 8px;
  padding: 20px;
  min-width: 260px;
  max-width: 480px;
  width: 50%;
  margin: auto;
  z-index: 11;
  background-color: black;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.9);
}
.hystmodal_wrap {
  height: 100%;
  display: flex;
  justify-content: center;
  align-content: center;
}
.modalBodyWrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  overflow: hidden auto;
}
.modal-block-title{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 40px;
  margin-top: 10px;
}
.modal-close {
  border-radius: 50%;
  color: #fff;
  background: #f70193;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  cursor: pointer;
  margin-right: 10px;
  text-align: center;
}

.modal-title {
  font-weight: 600;
  font-size: 24px;
  color: #FFFFFF;
}

.modal-content {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px
}
.modal-footer{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.modal-footer_button {

  min-height: 42px;
  background: black;
  /* блюр_кнопка */
  width: 40%;
  border-radius: 23px;
  font-weight: 600;
  font-size: 20px;
  color: #FFFFFF;
  border: none;
  box-sizing: border-box;
  cursor: pointer;
  margin: 10px 0;
}

.form__input {
  background: transparent;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  color: white;
  height: 25px;
  width: 95%;
  margin-bottom: 20px;
  margin-right: 10px;
}

.task__sort {
  align-items: center;
  margin-right: 5%;
  font-size: 14px;

}

.dropdown__list {
  display: none;
  position: absolute;
  top: 40px;
  left: 0;
  width: 95%;
  background: #000000;
  list-style: none;
  padding: 0;
  font-size: 14px;
  margin-right: 10px;
}

.dropdown {
  display: flex;
  align-items: center;
  border: 1.3px solid #919191;
  border-radius: 10px;
  background: #000000;
  cursor: pointer;
  color: #FFFFFF;
  position: relative;
  width: 100%;
  justify-content: space-between;
  padding: 0 10px;
  font-size: 14px;
  margin-right: 10px;
}

.dropdown__item {
  padding: 8px 15px;
}

.dropdown__item:hover {
  background: #919191;
}

.sort__dropdown-title {
  font-size: 14px;
}

.dropdown__image {
  margin: 0 0 0 5px;
}

.is-show {
  display: block;
}

.sort__text {
  margin-right: 20px;
  font-size: 14px;
  padding: 5px;
  margin-bottom: 10px;
}

.modal__add-user {
  font-size: 14px;
  background: none;
  border: none;
  color: #FFFFFF;
  padding: 10px;
}

*::-webkit-scrollbar {
  /*width: 5px; !* ширина scrollbar *!*/
  /*margin-left: 20px;*/
  display: none;
}
/**::-webkit-scrollbar-track {*/
/*  background: black;        !* цвет дорожки *!*/
/*}*/
/**::-webkit-scrollbar-thumb {*/
/*  background-color: white;    !* цвет плашки *!*/
/*  border-radius: 20px;       !* закругления плашки *!*/
/*  border: none;  !* padding вокруг плашки *!*/
/*}*/

</style>