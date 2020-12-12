<template>
  <div id="app">
    <!-- <header>
      <img alt="Braida logo" class="header-logo" src="./assets/logo.png">
    </header> -->
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <!-- <main>
        
    </main> -->
    <!-- <footer>
      Copyright&copy; 2020 - Robert Radošić
    </footer> -->
    <b-navbar :centered="true" :mobile-burger="false">
      <template
        class="is-flex is-justify-content-center is-align-items-center"
        slot="brand"
      >
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img src="./assets/logo.png" alt="Braida logo" />
        </b-navbar-item>
      </template>
    </b-navbar>
    <div class="container">
      <section class="section">
        <transition
          name="slideLeft"
          mode="out-in"
        >
          <router-view
            @saveSuccess="backendSaveSuccess"
            @saveError="backendSaveError"
            style="animation-duration: 0.5s"
          />
        </transition>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    backendError() {
      this.$buefy.snackbar.open({
        message: this.$t("messages.backendError"),
        type: "is-danger",
        position: "is-bottom",
        indefinite: true,
      });
    },
    backendSaveSuccess() {
      this.$buefy.snackbar.open({
        message: this.$t("messages.backendSaveSuccess"),
        type: "is-success",
        position: "is-bottom",
      });
    },
    backendSaveError() {
      this.$buefy.snackbar.open({
        message: this.$t("messages.backendSaveError"),
        type: "is-danger",
        position: "is-bottom",
      });
    },
  },
  mounted() {
    var me = this;
    this.axios.get("/").catch(() => me.backendError());
  },
};
</script>

<style lang="scss">
@import "./assets/scss/_colors";

.navbar-brand {
  display: flex;
  justify-content: center;
  background-color: $custom-white;
  align-items: center;
}
body {
  min-height: 100vh;
  background-color: $custom-white;
  // transition: background 1.5s linear;
}

.navbar-item img {
  /* max-height: 1.75rem; */
  max-height: 3rem !important;
}
</style>
