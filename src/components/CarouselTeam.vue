<template>
    <team class="team">
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
            <button class="btn-prev">Prev</button>
            <button class="btn-next">Next</button>
          </div>
        </div>
      </section>
    </team>
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
  })
};

</script>

<style lang="scss" scoped>

.carousel {
  overflow: hidden;
  display: flex;
  flex-direction: row;
  padding-left: 144px;
}


.item {

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

</style>