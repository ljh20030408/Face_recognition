import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { NoticeBar } from 'vant';
import { Swipe } from "vant";
import { SwipeItem } from "vant";
import {Button} from "vant";
import { Circle } from 'vant';
import { ActionSheet } from 'vant';
import { Dialog } from 'vant';
import { Toast } from "vant";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from "axios";

Vue.config.productionTip = false
Vue.use(NoticeBar)
Vue.use(Swipe)
Vue.use(SwipeItem)
Vue.use(Button)
Vue.use(Circle)
Vue.use(ActionSheet)
Vue.use(Dialog)
Vue.use(Toast)
Vue.use(ElementUI)

Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
