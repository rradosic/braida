<template>
  <div class="about submenu" key="lighting">
    <h1 class="title">{{ $t("title.lighting") }}</h1>

    <h2 class="subtitle is-6">Customize your lighting options</h2>

    <div class="field">
      <b-switch @input="saveFormData" v-model="saveData.enabled">{{
        $t("common.enabled")
      }}</b-switch>
    </div>

    <div class="mt-5">
      <transition name="fade" mode="out-in">
        <b-field v-if="saveData.enabled" :label="$t('common.type')">
          <b-select
            @input="changeType"
            v-model="saveData.type"
            placeholder="Select a type"
            required
          >
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
          :options="saveData.typeOptions"
          v-if="saveData.type == 'music' && saveData.enabled"
        ></music-reactive>
        <static
          key="flag"
          :options="saveData.typeOptions"
          v-if="saveData.type == 'static' && saveData.enabled"
        ></static>
        <flag
          key="flag"
          :options="saveData.typeOptions"
          v-if="saveData.type == 'flag' && saveData.enabled"
        ></flag>
      </transition>
      <transition name="fade">
        <div v-if="saveData.enabled" class="buttons mt-5">
          <b-button @click="saveFormData" type="is-primary" >{{
            $t("common.apply")
          }}</b-button>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import Flag from "../components/Lighting/Flag.vue";
import MusicReactive from "../components/Lighting/MusicReactive.vue";
import Static from "../components/Lighting/Static.vue";
export default {
  name: "Lighting",
  components: { MusicReactive, Flag, Static },
  data: () => {
    return {
      saveData: {
        enabled: false,
        type: null,
        typeOptions: {},
      },
    };
  },
  mounted() {
    var me = this;
    this.axios
      .get("/lighting")
      .then((response) => (me.saveData = response.data));
  },
  methods: {
    changeType() {
      this.typeOptions = {};
    },
    saveFormData() {
      var me = this;
      this.axios
        .post("/lighting", this.saveData)
        .then((response) => {
          if(response.data.success){
            me.$emit('saveSuccess');
          }
        }).catch(() => me.$emit('saveError'));
    },
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