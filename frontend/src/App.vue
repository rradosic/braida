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
          <img
            src="./assets/logo.png"
            alt="Lightweight UI components for Vue.js based on Bulma"
          />
        </b-navbar-item>
      </template>
    </b-navbar>
    <div class="container">
      <section class="section">
        <transition name="zoom" mode="out-in">
          <router-view />
        </transition>
      </section>
    </div>
  </div>
</template>

<script>
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
}

.navbar-item img {
  /* max-height: 1.75rem; */
  max-height: 3rem !important;
}
</style>
