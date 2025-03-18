import Vue from 'vue'
import VueRouter from 'vue-router'
import FaceRecognition from "@/views/FaceRecognition";
import Navigation from "@/views/Navigation";
import FaceInfo from "@/views/FaceInfo";
import FaceInfoGet from "@/views/FaceInfoGet";
import CheatInfo from "@/views/CheatInfo";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Navigation',
    component: Navigation
  },
  {
    path: '/faceRecognition',
    name: 'FaceRecognition',
    component: FaceRecognition
  },
  {
    path: '/faceInfo',
    name: 'FaceInfo',
    component: FaceInfo
  },
  {
    path: '/faceInfoGet',
    name: 'FaceInfoGet',
    component: FaceInfoGet
  },
  {
    path: '/cheatInfo',
    name: 'CheatInfo',
    component: CheatInfo
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
