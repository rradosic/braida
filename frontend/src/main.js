import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueI18n from 'vue-i18n';
import translations from './translations/translations';
import vSelect from 'vue-select'
import Buefy from 'buefy'

// import 'buefy/dist/buefy.css'
import 'normalize.css';
import './assets/scss/style.scss';
import 'vue2-animate/dist/vue2-animate.min.css';

import 'ionicons/dist/ionicons';

Vue.use(VueI18n);
Vue.use(Buefy);
Vue.component('v-select', vSelect)

const i18n = new VueI18n({
  locale: 'en', // set locale
  messages: translations, // set locale messages
});

Vue.config.productionTip = false

const DEFAULT_TITLE = 'Braida';

router.afterEach((to) => {

    Vue.nextTick(() => {
        document.title = i18n.t(to.meta.title) || DEFAULT_TITLE;
    });
});

new Vue({
  router,
  i18n,
  render: h => h(App),
}).$mount('#app')
