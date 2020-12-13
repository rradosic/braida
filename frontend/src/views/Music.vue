<template>
  <div class="about submenu" key="music">
    <h1 class="title">{{ $t("title.music") }}</h1>

    <h2 class="subtitle is-6">Customize your music options</h2>

    <div class="field">
      <b-switch @input="saveFormData" v-model="saveData.enabled">{{
        $t("common.enabled")
      }}</b-switch>
    </div>

    <div class="mt-5">
      <transition name="fade" mode="out-in">
        <div v-if="saveData.enabled">
          <b-field :label="$t('music.volume')">
            <b-slider size="is-medium" v-model="saveData.volume"> </b-slider>
          </b-field>
          <b-field :label="$t('common.type')">
            <b-select
              @input="changeType"
              v-model="saveData.type"
              placeholder="Select a type"
              required
            >
              <option value="bluetooth">Bluetooth</option>
              <option value="fm">Fm radio</option>
            </b-select>
          </b-field>
        </div>
      </transition>
      <transition name="fade" mode="out-in"> </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "Music",
  components: {},
  data: () => {
    return {
      saveData: {
        enabled: false,
        volume: 50,
        type: null,
        typeOptions: {},
      },
    };
  },
  mounted() {
    var me = this;
    this.axios.get("/music").then((response) => (me.saveData = response.data));
  },
  methods: {
    changeType() {
      this.typeOptions = {};
      this.saveFormData();
    },
    saveFormData() {
      this.axios
        .post("/music", this.saveData)
        .then((response) => console.log(response));
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