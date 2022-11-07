<template>
  <main class="main about container">
    <section class="about__team about-team">
      <h2 class="about-team__title">Наша команда</h2>

      <div class="about-team__direction direction">
        <h3 class="direction__title">Менеджеры</h3>
        <ul class="direction__members">
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

      <div class="about-team__direction direction">
        <h3 class="direction__title">Бэкенд</h3>
        <ul class="direction__members">
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

      <div class="about-team__direction direction">
        <h3 class="direction__title">Фронтенд</h3>
        <ul class="direction__members members-two">
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

      <div class="about-team__direction direction">
        <h3 class="direction__title">Дизайнеры</h3>
        <ul class="direction__members members-two">
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
    </section>

    <section class="about__projects about-projects">
      <h2 class="about-projects__title">Наши проекты</h2>

      <div class="about-project__projects">
        <div class="about-project__project" v-for="(project, index) in projects" :key="index">
          <img
            class="about-project__image"
            :src="project.icon"
            alt="SecondProject"
          />
          <h3 class="about-project__project-title">{{ project.title }}</h3>
          <router-link class="about-project__button more-btn" type="button" :to="{ name: 'OurProjects', params: {project: project}}">Подробнее</router-link>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import MemberCard from "../../components/MemberCard/";

import NastyaImage from "../../assets/images/team/nastya.jpg";
import RenskiyImage from "../../assets/images/team/renskiy.jpg";
import VladImage from "../../assets/images/team/back.jpg";
import IlyaImage from "../../assets/images/team/back.jpg";
import MiheyImage from "../../assets/images/team/mihey.jpg";
import VasyaImage from "../../assets/images/team/vasya.jpg";
import DenisImage from "../../assets/images/team/denis.jpg";
import SofaImage from "../../assets/images/team/sofa.jpg";
import AlyonaImage from "../../assets/images/team/alyona.jpg";
import AlonkaImage from "../../assets/images/team/alonka.jpg";

import { mapGetters, mapActions } from 'vuex';

export default {
  name: "AboutPage",
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
  }),
  computed: {
    ...mapGetters({
      projects: 'getProjects',
    })
  },
  mounted() {
    this.loadProjects()
  },
  methods: {
    ...mapActions({
      loadProjects: 'loadProjects',
    })
  },
};
</script>

<style lang="scss" scoped>
h3.direction__title {
  margin-bottom: 20px;
}

.about-project__project {
  img {
    margin-bottom: 10px;
  }
  h3 {
    margin-bottom: 10px;
  }
}
.about-project__button {
  text-align: center;
}

.about-project__projects[data-v-64e2f1a6] {
  justify-content: center;
}

.direction {
  &__members {
    display: flex;
    justify-content: space-between;
  }
  .members-two {
    justify-content: center;

    .direction__member:first-of-type {
      margin: 0 30px 0 0;
    }
    .direction__member:not(:first-of-type) {
      margin: 0 0 0 30px;
    }
  }
  &__member-image {
    width: 100%;
    border-radius: 50%;
  }
  &__member {
    flex-basis: 20%;
  }
  &__mamber-name {
    text-align: center;
  }
  &__mamber-description {
    text-align: center;
  }
  &:not(:first-of-type) {
    margin: 60px 0 0 0;
  }
}

.about-projects {
  margin: 50px 0 0 0;
}
.about-project {
  &__projects {
    display: grid;
    grid-template-columns: minmax(200px, 400px) minmax(200px, 400px);
    grid-gap: 20px;
    justify-content: space-between;
    margin: 40px 0 0 0;
  }
  &__project {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }
  &__image {
    width: 100%;
    border-radius: 30px;
    max-height: 500px;
  }
  &__button {
    display: block;
    margin: 0 auto;
  }
}
@media (max-width: 768px) {
  .direction {
    &__members {
      flex-direction: column;
    }
    .members-two {
      justify-content: center;

      .direction__member:first-of-type {
        margin: 10px 0 0 0;
        padding-bottom: 5%;
      }
      .direction__member:not(:first-of-type) {
        margin: 10px 0 0 0;
        padding-bottom: 5%;
      }
    }
  }
}
</style>