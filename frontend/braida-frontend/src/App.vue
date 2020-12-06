<template>
  <div id="app">
    <header>
      <img alt="Braida logo" class="header-logo" src="./assets/logo.png">
    </header>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <main>
      <transition name="zoom" mode="out-in">
        <router-view/>
      </transition>
    </main>
    <!-- <footer>
      Copyright&copy; 2020 - Robert Radošić
    </footer> -->
  </div>
</template>

<style lang="scss">
#app {
  font-family: Raleway, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  
}
</style>
