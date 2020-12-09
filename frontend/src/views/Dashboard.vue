<template>
  <!-- <div id="dashboard" key="dashboard">
        <router-link to="/lighting">
            <div class="dashboard-card">
                <div class="card-img flex flex-center">
                    <img src="../assets/images/dashboard/lighting.svg" alt="">
                </div>
                <p class="card-bottom-text">{{ $t("title.lighting") }}</p>
            </div>
        </router-link>
        <router-link to="/music">
            <div class="dashboard-card">
                <div class="card-img flex flex-center">
                    <img src="../assets/images/dashboard/music.svg" alt="">
                </div>
                <p class="card-bottom-text">Music</p>
            </div>
        </router-link>
        <router-link to="/settings">
        <div class="dashboard-card">
            <div class="card-img flex flex-center">
                <img src="../assets/images/dashboard/settings.svg" alt="">
            </div>
            <p class="card-bottom-text">Settings</p>
        </div>
        </router-link>
    </div> -->
  <div class="columns">
    <div class="column is-flex is-justify-content-center is-align-items-center">
      <dashboard-card
        :image="require('@/assets/images/dashboard/lighting.svg')"
        :route="'/lighting'"
        :title="$t('title.lighting')"
      ></dashboard-card>
    </div>

    <div class="column is-flex is-justify-content-center is-align-items-center">
      <dashboard-card
        :image="require('@/assets/images/dashboard/music.svg')"
        :route="'/music'"
        :title="$t('title.music')"
      ></dashboard-card>
    </div>
    <div class="column is-flex is-justify-content-center is-align-items-center">
      <dashboard-card
        :image="require('@/assets/images/dashboard/settings.svg')"
        :route="'/settings'"
        :title="$t('title.settings')"
      ></dashboard-card>
    </div>
  </div>
</template>

<script>
import DashboardCard from "../components/Dashboard/DashboardCard.vue";
export default {
  components: { DashboardCard },
  name: "Dashboard",
  mounted(){
    this.axios.get('/').then(response => (console.log(response)));
  }
};

</script>

<style>
</style>