<template>
  <div class="about submenu" key="lighting">
    <h1 class="title">{{ $t("title.lighting") }}</h1>

    <h2 class="subtitle is-6">Customize your lighting options</h2>

    <div class="field">
      <b-switch v-model="enabled">{{ $t("common.enabled") }}</b-switch>
    </div>

      <div class="mt-5" >
        <transition name="fade" mode="out-in">
          <b-field v-if="enabled" :label="$t('common.type')">
            <b-select v-model="type" placeholder="Select a type" required>
              <option value="music">Music reactive</option>
              <option value="static">Static</option>
              <option value="festive">Festive</option>
              <option value="flag">Flag</option>
            </b-select>
          </b-field>
      </transition>
    <transition name="fade" mode="out-in">
        <music-reactive
          key="music-reactive"
          v-if="type == 'music' && enabled "
        ></music-reactive>
    </transition>
      </div>
  </div>
</template>

<script>
import MusicReactive from "../components/Lighting/MusicReactive.vue";
export default {
  name: "Lighting",
  components: { MusicReactive },
  data: () => {
    return {
      enabled: false,
      type: null,
    };
  },
};
</script>

<style lang="scss">
.background-img {
  position: absolute;
  opacity: 15%;
  transform: rotate(-30deg);
  height: 100vh;
}
</style>