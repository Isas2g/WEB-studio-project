<template>
      <section class="team__body">
        <h1 class="team__title">Наша команда</h1>
<!--        <button class="team__btn prev">-->
<!--          <img-->
<!--              class="team__arrow"-->
<!--              :src="BtnArr"-->
<!--              alt="BtnArr"-->
<!--          />-->
<!--        </button>-->
        <div class="team__container carousel">
          <div class="carousel-track">
            <div class="carousel-item item">
              <h3 class="item__title">Менеджеры</h3>
              <ul class="item__members">
                <MemberCard
                    name="Настя"
                    description="А тут описание под заголовком"
                    :image="NastyaImage"
                />
                <MemberCard
                    name="Ренат"
                    description="А тут описание под заголовком"
                    :image="RenskiyImage"
                />
                <MemberCard
                    name="Влад"
                    description="А тут описание под заголовком"
                    :image="VladImage"
                />
              </ul>
            </div>

            <div class="carousel-item item">
              <h3 class="item__title">Бэкэнд</h3>
              <ul class="item__members">
                <MemberCard
                    name="Илья"
                    description="А тут описание под заголовком"
                    :image="IlyaImage"
                />
                <MemberCard
                    name="Данил"
                    description="А тут описание под заголовком"
                    :image="MiheyImage"
                />
                <MemberCard
                    name="Вася"
                    description="А тут описание под заголовком"
                    :image="VasyaImage"
                />
              </ul>
            </div>

            <div class="carousel-item item">
              <h3 class="item__title">Фронтэнд</h3>
              <ul class="item__members members-two">
                <MemberCard
                    name="Денис"
                    description="А тут описание под заголовком"
                    :image="DenisImage"
                />
                <MemberCard
                    name="Софа"
                    description="А тут описание под заголовком"
                    :image="SofaImage"
                />
              </ul>
            </div>

            <div class="carousel-item item">
              <h3 class="item__title">Дизайнеры</h3>
              <ul class="item__members members-two">
                <MemberCard
                    name="Алёна"
                    description="А тут описание под заголовком"
                    :image="AlyonaImage"
                />
                <MemberCard
                    name="Алёна"
                    description="А тут описание под заголовком"
                    :image="AlonkaImage"
                />
              </ul>
            </div>
          </div>
          <div class="carousel-btn">
            <button v-on:click="prevTeamSlide" class="btn-prev">
              <img
                class="projects__arrow"
                :src="BtnLeftArr"
                alt="BtnLeftArr"
              />
            </button>
            <button v-on:click="nextTeamSlide" class="btn-next">
              <img
                class="projects__arrow"
                :src="BtnArr"
                alt="BtnArr"
              />
            </button>
          </div>
        </div>
      </section>
</template>

<script>
import NastyaImage from "@/assets/images/team/nastya.jpg";
import RenskiyImage from "@/assets/images/team/renskiy.jpg";
import VladImage from "@/assets/images/team/back.jpg";
import IlyaImage from "@/assets/images/team/back.jpg";
import MiheyImage from "@/assets/images/team/mihey.jpg";
import VasyaImage from "@/assets/images/team/vasya.jpg";
import DenisImage from "@/assets/images/team/denis.jpg";
import SofaImage from "@/assets/images/team/sofa.jpg";
import AlyonaImage from "@/assets/images/team/alyona.jpg";
import AlonkaImage from "@/assets/images/team/alonka.jpg";
import MemberCard from "@/components/MemberCard";
import BtnLeftArr from "@/assets/images/btn-left-strelka.png";
import BtnArr from "@/assets/images/btn-strelka.png";

export default {
  components: {
    MemberCard,
  },
  data: () => ({
    NastyaImage: NastyaImage,
    RenskiyImage: RenskiyImage,
    VladImage: VladImage,
    IlyaImage: IlyaImage,
    MiheyImage: MiheyImage,
    VasyaImage: VasyaImage,
    DenisImage: DenisImage,
    SofaImage: SofaImage,
    AlyonaImage: AlyonaImage,
    AlonkaImage: AlonkaImage,
    BtnArr: BtnArr,
    BtnLeftArr: BtnLeftArr,
    slideCount: 1
  }),
  methods: {
    nextTeamSlide: function() {
      if (this.slideCount < 300) {
        this.slideCount = this.slideCount + 101;
        document.getElementsByClassName('carousel-track')[0].style.left = `-${this.slideCount}%`;
      } else {
        this.slideCount = 1;
        document.getElementsByClassName('carousel-track')[0].style.left = `-${this.slideCount}%`;
      }
    },
    prevTeamSlide: function() {
      if (this.slideCount > 0) {
        this.slideCount = this.slideCount - 101;
        document.getElementsByClassName('carousel-track')[0].style.left = `-${this.slideCount}%`;
      } else {
        this.slideCount = 304;
        document.getElementsByClassName('carousel-track')[0].style.left = `-${this.slideCount}%`;
      }
    }
  }
};

</script>

<style lang="scss" scoped>

.team__body {
  margin-bottom: 40px;
}


.carousel {
  overflow: hidden;
  position: relative;
  height: 370px;
}

.carousel-track {
    display: flex;
    top: 0;
    position: absolute;
    left: 0%;
    transition: 0.3s;
  }
  .carousel-track.management {
    left: 0%;
  }
  .carousel-track.backend {
    left: -100%;
  }
  .carousel-track.frontend {
    left: -200%;
  }
  .carousel-track.design {
    left: -300%;
  }

.carousel-item.item {
  flex-shrink: 0;
  min-width: 36%;
  padding-left: 50px;
  padding-right: 50px;
}

.carousel-btn {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  display: flex;
  justify-content: space-between;
}
.btn-prev, .btn-next {
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}

.item {

  &__title {
    margin-bottom: 20px;
  }

  .member {
    width: 240px;
    flex-basis: unset;
    margin-left: 15px;
    margin-right: 15px;
  }

  &__members {
    display: flex;
    justify-content: space-between;
  }

  .members-two {
    justify-content: center;

    .item__member:first-of-type {
      margin: 0 30px 0 0;
    }

    .item__member:not(:first-of-type) {
      margin: 0 0 0 30px;
    }
  }
}

.team {
  &__title {
    margin-bottom: 20px;
  }
}

</style>