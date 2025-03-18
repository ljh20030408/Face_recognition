<template>
  <div id="app" v-cloak>
    <van-notice-bar color="#1989fa" background="#ecf9ff" :scrollable="false">
      <van-swipe ref="actionSwipe" vertical class="notice-swipe" :show-indicators="false" :touchable="false">
        <van-swipe-item v-for="(item,index) in currentAction" :key="index">{{item.name}}</van-swipe-item>
        <van-swipe-item v-if="!isObjEmpty(currentAction)">已完成</van-swipe-item>
      </van-swipe>
    </van-notice-bar>
    <div class="Camera-wrapper" :style="{width:width+7+'px',height:height+7+'px'}">

      <div class="canvas-wrapper" :style="{width:width+'px',height:height+'px'}">


        <video ref="video" :width="width" :height="height" webkit-playsinline="true" playsinline="true" preload autoplay
               loop muted></video>
        <canvas ref="canvas" :width="width" :height="height"></canvas>

      </div>
      <!--      <van-circle v-model="currentRate" :style="{width:width+7+'px',height:height+7+'px'}" :rate="100" :speed="10"-->
      <!--                  stroke-width="15"></van-circle>-->

    </div>
    <div class="btn-operate">
      <van-button @click="startMediaRecorder" v-if="isCameraOpen && !inProgress" type="info" native-type="button">开始录制
      </van-button>
      <van-button v-if="isCameraOpen && inProgress" type="danger" native-type="button" disabled>录制中</van-button>
      <van-button @click="neuAufnehmen" v-if="!isCameraOpen && !inProgress" type="default" native-type="button">重新录制
      </van-button>
    </div>
    <div class="prompt-text">
      <h5>视频录制说明</h5>
      <ol>
        <li>请使用前置摄像头。</li>
        <li>脸部距离屏幕应该控制<span ref="faceProportion"></span>。</li>
        <li>保证光线充足、脸部完全入镜、脸部无遮挡物。</li>
        <li>开始录制后请按照提示做出相应动作。</li>
        <li>如录制不满意可点击“重新录制”。</li>
        <li>底部按钮：左边切换摄像头、右边切换镜像</li>
      </ol>
    </div>
    <div style="height: calc(5vh + 70px )"></div>
    <!-- 切换摄像头 -->
    <div class="Camera-toggle" title="切换摄像头" @click="actionShow = true">
      <svg t="1658028836694" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
           p-id="5841" width="200" height="200">
        <path
            d="M868.355 291.969l-95.558-15.726-29.174-72.070c-16.743-41.3-56.578-67.992-101.478-67.992l-260.384 0c-44.855 0-84.709 26.682-101.565 68.042l-29.128 72.019-95.517 15.726c-53.023 8.687-91.504 53.659-91.504 106.941v385.782c0 59.772 49.065 108.406 109.372 108.406h677.035c60.322 0 109.403-48.623 109.403-108.396v-385.792c0-53.282-38.481-98.254-91.499-106.941zM897.356 784.703c0 25.308-21.036 45.897-46.904 45.897h-677.035c-25.848 0-46.874-20.599-46.874-45.908l0-385.782c0-22.512 16.449-41.553 39.132-45.267l112.856-18.584c10.752-1.77 19.805-9.012 23.894-19.113l35.68-88.214c7.192-17.649 24.327-29.052 43.654-29.052h260.384c19.327 0 36.427 11.373 43.558 28.961l35.755 88.315c4.079 10.091 13.132 17.334 23.884 19.103l112.882 18.584c0.010 0 0.020 0 0.020 0.010 22.664 3.702 39.112 22.745 39.112 45.257l0 385.793z"
            p-id="5842" fill="#ffffff"></path>
        <path
            d="M436.876 473.188c-17.257 0-31.249 13.987-31.249 31.249v30.486c0 17.262 13.992 31.249 31.249 31.249s31.249-13.987 31.249-31.249v-30.486c0-17.261-13.992-31.249-31.249-31.249z"
            p-id="5843" fill="#ffffff"></path>
        <path
            d="M587.024 473.188c-17.262 0-31.249 13.987-31.249 31.249v30.486c0 17.262 13.987 31.249 31.249 31.249s31.249-13.987 31.249-31.249v-30.486c0-17.261-13.987-31.249-31.249-31.249z"
            p-id="5844" fill="#ffffff"></path>
        <path
            d="M768.412 403.814c-12.207-12.207-31.981-12.207-44.188 0l-19.261 19.262c-39.232-69.398-114.001-114.87-195.852-114.87-98.691 0-187.276 66.007-215.417 160.518-4.923 16.54 4.496 33.945 21.036 38.868 16.57 4.923 33.945-4.496 38.868-21.026 20.309-68.215 84.257-115.862 155.513-115.862s135.209 47.647 155.523 115.862c0.162 0.541 0.418 1.025 0.605 1.551 0.261 0.734 0.529 1.455 0.847 2.171 0.521 1.178 1.126 2.287 1.775 3.371 0.309 0.516 0.577 1.044 0.919 1.544 1.101 1.619 2.316 3.135 3.678 4.499 0.011 0.011 0.017 0.025 0.030 0.036 0.071 0.071 0.156 0.115 0.226 0.185 1.284 1.258 2.68 2.377 4.151 3.39 0.533 0.368 1.083 0.68 1.632 1.012 1.070 0.645 2.165 1.226 3.304 1.74 0.627 0.281 1.249 0.557 1.891 0.796 1.224 0.457 2.478 0.811 3.757 1.114 0.525 0.123 1.035 0.289 1.564 0.384 1.824 0.333 3.676 0.544 5.561 0.544 1.77 0 3.56-0.208 5.352-0.523 0.558-0.096 1.102-0.238 1.655-0.365 0.643-0.148 1.283-0.234 1.925-0.425 0.45-0.134 0.837-0.371 1.277-0.525 1.057-0.365 2.081-0.793 3.102-1.274 0.917-0.432 1.804-0.889 2.662-1.401 0.837-0.5 1.64-1.048 2.438-1.634 0.927-0.679 1.807-1.391 2.645-2.161 0.338-0.31 0.723-0.531 1.050-0.858l51.736-51.736c12.205-12.197 12.205-31.993-0.002-44.188z"
            p-id="5845" fill="#ffffff"></path>
        <path
            d="M709.159 558.289c-16.519-4.923-33.935 4.496-38.858 21.036-20.303 68.215-84.257 115.852-155.513 115.852-71.262 0-135.215-47.647-155.518-115.852-0.135-0.455-0.376-0.845-0.53-1.29-0.363-1.053-0.79-2.076-1.27-3.093-0.432-0.919-0.89-1.805-1.403-2.665-0.498-0.834-1.044-1.633-1.626-2.428-0.685-0.936-1.404-1.824-2.182-2.669-0.306-0.334-0.525-0.715-0.848-1.039-0.328-0.33-0.717-0.553-1.057-0.864-0.847-0.775-1.724-1.489-2.647-2.163-0.781-0.573-1.566-1.112-2.384-1.604-0.879-0.526-1.78-0.989-2.706-1.425-0.919-0.434-1.835-0.84-2.783-1.179-0.939-0.337-1.891-0.602-2.862-0.848-0.976-0.247-1.943-0.468-2.934-0.619-0.992-0.152-1.985-0.231-2.994-0.288-1.029-0.056-2.046-0.080-3.076-0.036-0.953 0.041-1.898 0.142-2.856 0.273-1.129 0.153-2.237 0.363-3.346 0.639-0.454 0.114-0.909 0.125-1.362 0.26-0.444 0.132-0.825 0.366-1.258 0.517-1.073 0.37-2.116 0.804-3.152 1.296-0.898 0.425-1.768 0.873-2.609 1.374-0.852 0.508-1.669 1.064-2.479 1.661-0.918 0.674-1.79 1.379-2.622 2.143-0.34 0.311-0.729 0.535-1.057 0.864l-51.736 51.736c-12.207 12.197-12.207 31.992 0 44.188 6.098 6.103 14.099 9.156 22.094 9.156s15.996-3.051 22.094-9.156l19.26-19.26c39.234 69.4 114.004 114.869 195.853 114.869 98.701 0 187.281-66.007 215.408-160.528 4.92-16.54-4.499-33.935-21.039-38.858z"
            p-id="5846" fill="#ffffff"></path>
      </svg>
    </div>
    <van-action-sheet v-model="actionShow" :actions="deviceList" description="请选择设备" @select="actionSelect"
                      cancel-text="取消" close-on-click-action>
    </van-action-sheet>
    <!-- 切换摄像头 -->

    <!-- 镜像 -->
    <div class="FlipHorizontal-toggle" :class="{FlipHorizontalIng:flipHorizontal}" title="左右镜像"
         @click="triggerToggleFlipHorizontal">
      <svg t="1663289810507" class="icon" viewBox="0 0 1117 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
           p-id="3494" width="128" height="128">
        <path
            d="M442.898361 116.049051l2.23404 0.74468L74.840328 1.368349A61.901515 61.901515 0 0 0 0 61.966675v883.283427a61.9946 61.9946 0 0 0 74.840328 60.598326l379.507486-118.124847a77.074368 77.074368 0 0 0 41.981329-68.510549V189.58619a77.539793 77.539793 0 0 0-53.430782-73.537139zM403.244157 792.218386L93.084986 874.412428V132.618179l310.159171 82.380212v577.12691zM1054.466716 0.065159a77.260538 77.260538 0 0 0-12.845728 1.30319L675.796995 115.490542l1.30319-0.18617a77.446708 77.446708 0 0 0-56.968012 74.467988v629.161417c0 29.88028 17.034552 55.850991 41.981329 68.696719l379.228231 118.217932a61.9946 61.9946 0 0 0 75.026498-60.691411V61.966675a61.529175 61.529175 0 0 0-61.901515-61.808431z"
            fill="#ffffff" opacity=".801" p-id="3495">
        </path>
      </svg>
    </div>
    <!-- 镜像 -->

    <video ref="videoRef" :src="url" autoplay @canplay="capture" ></video>

  </div>
</template>

<script>

import * as faceLandmarksDetection from "@tensorflow-models/face-landmarks-detection";
import {tile} from "@tensorflow/tfjs";

export default {

  name: 'HomeView',
  data:function (){
    return{
      width: 280,
      height: 280,
      actionShow: false,
      deviceList: [], //设备列表
      deviceId: window.localStorage.getItem(`deviceId`) || '', //设备id
      isCameraOpen: false,//相机是否打开
      inProgress: false, //是否正在录制
      faceDistanceisOK: false,
      mediaRecorder: null, //录制器
      mediaStreamTrack: null, //音频或视频流
      blob: null, //录制的视频
      ModelLoading: false,//模型加载中
      detector: null, //识别模型
      rafId: null,
      flipHorizontal: false,//镜像
      faceNullFrequency: 0,
      isFarArr: [], //记录远近
      isOpenMouthArr: [], //张嘴
      isWinkArr: [], //眨眼
      isShakingHisHeadArr: [], //摇头
      actionList: [
        // {
        //   name: "远一些",
        //   value: 0,
        // },
        // // {
        // //   name: "张嘴",
        // //   value: 2,
        // // },
        // {
        //   name: "近一些",
        //   value: 1,
        // },
        {
          name: "张嘴",
          value: 2,
        },
        {
          name: "眨眼",
          value: 3,
        },
        // {
        //   name: "向左转头",
        //   value: 4,
        // },
        // {
        //   name: "向右转头",
        //   value: 5,
        // },
      ],//动作列表
      currentAction: [],//当前动作
      currentRate: 0,
      nextactionTime: 0,

      url:'',
      ip: '',
    }
  },
  mounted() {
    const size = (document.documentElement.clientWidth || window.innerWidth) * 0.6;
    this.width = size > 280 ? 280 : size;
    this.height = size > 280 ? 280 : size;

    // 一堆兼容代码
    this.compatible();
    this.openUserMedia();
    this.getIp();


  },
  methods:{

    getIp(){
      let xhr = new XMLHttpRequest();
      xhr.open('GET', 'https://ip.useragentinfo.com/json');
      xhr.responseType = 'json';
      xhr.send();
      xhr.onreadystatechange = ()=> {
        if (xhr.readyState === 4) {
          let ipinfo = xhr.response;
          //console.log(ipinfo.ip)
          this.ip = ipinfo.ip
        }
      } //获取ip
    },

    capture() {
      //console.log(this);
      const videoPlayer = this.$refs.videoRef;
      const canvas = document.createElement("canvas");

      canvas.width = videoPlayer.videoWidth;
      canvas.height = videoPlayer.videoHeight;

      const context = canvas.getContext("2d");

      context.drawImage(videoPlayer, 0, 0, canvas.width, canvas.height);
      // 将 canvas 上的图像数据转为 base64 编码的字符串
      const imageData = canvas.toDataURL("image/jpeg");
      // 将 base64 编码的字符串转为二进制数据
      const data = atob(imageData.split(",")[1]);
      const buffer = new Uint8Array(data.length);
      for (let i = 0; i < data.length; i++) {
        buffer[i] = data.charCodeAt(i);
      }
      const blob = new Blob([buffer], { type: "image/jpeg" });

      let formData_verify = new FormData();
      formData_verify.append("image",blob);
      //console.log("ok");
      //console.log(this.ip);
      formData_verify.append("ip",this.ip)

      let formData_auth = new FormData();
      formData_auth.append("file",blob);
      formData_auth.append("ipaddr",this.ip)
      //console.log("----------------------------------------------")
      //console.log(this.ip)


      this.$axios({
            url:'http://101.43.93.152:6004/verify',
            method:'post',
            headers: {
              "Content-Type":"multipart/form-data"
            },
            data: formData_verify,

          }
      ).then(
          res => {
            let message;
            console.log(res.data)
            if (res.data[1].result === 'true'){
              message = '校验成功，欢迎您'+ res.data[0].matched_name
              this.$message({
                    type:'success',
                    message: message
                  }
              )
            }else {
              message = '校验失败，未包含您的人脸信息!'
              this.$message({
                    type:'warning',
                    message: message
                  }
              )
            }
          }
      ).catch(
          err => {
            this.$message(
                {
                  message: '出现错误'
                }
            )
            console.log(err)
          }
      )


      this.$axios({
            url:'http://101.43.93.152:6005/photo',
            method:'post',
            headers: {
              "Content-Type":"multipart/form-data"
            },
            data: formData_auth,

          }
      ).then(
          res => {
            let message;
            console.log(res.data)
            if (res.data.fakeness <= 0.5){
              message = '您的真实度'+ res.data.fakeness+'所花费时间'+res.data.time+'s'
              this.$message({
                    type:'success',
                    message: message
                  }
              )
            }else {
              message = '您有可能是伪造的'
              this.$message({
                    type:'warning',
                    message: message
                  }
              )
            }
          }
      ).catch(
          err => {
            this.$message(
                {
                  message: '出现错误'
                }
            )
            console.log(err)
          }
      )




      // 创建并下载图片文件
      //const blob = new Blob([buffer], { type: "image/jpeg" });
      // const link = document.createElement("a");
      // link.href = URL.createObjectURL(blob);
      // link.download = "frame.jpg";
      // document.body.appendChild(link);
      // link.click();
      // document.body.removeChild(link);
    },

    isObjEmpty(obj) {
      return (
          obj === undefined ||
          obj === "undefined" ||
          obj == null ||
          obj === "" ||
          obj.length === 0 ||
          (typeof obj === "object" && Object.keys(obj).length === 0)
      );
    },
    async neuAufnehmen() {
      await this.getUserMedia();
      await this.createDetector();
      await this.startMediaRecorder();
    },
    //打开摄像头
    async openUserMedia() {
      const isOpen = await this.getUserMedia();
      if (isOpen.code == "ok") {
        await this.createDetector();
        this.$toast.loading(`摄像头已打开`);
      } else {
        this.$dialog.alert({
          title: '失败',
          message: `打开摄像头失败：${isOpen.errMsg}`,
          theme: 'round-button',
        }).then(() => {
          location.replace(`${location.pathname}?s=${new Date().getTime()}`)
        });
        return;
      };
    },
    getUserMedia() {
      return new Promise(async resolve => {
        this.inProgress = false;
        this.isCameraOpen = false;
        this.blob = null;
        const toast = this.$toast.loading({
          duration: 0, // 持续展示 toast
          forbidClick: true,
          message: '打开摄像头',
        });
        let mediaOpts = {
          audio: false,
          video: {
            width: this.width,
            height: this.height,
            frameRate: {
              ideal: 100,
              max: 150
            } //最佳帧率
          }
        };
        if (this.isObjEmpty(this.deviceId)) {
          mediaOpts.video.facingMode = "user"; //前置摄像头
          // mediaOpts.video.facingMode = "environment"; //后置摄像头
        } else {
          mediaOpts.video.deviceId = this.deviceId;
        }
        try {
          const stream = await navigator.mediaDevices.getUserMedia(mediaOpts);
          this.mediaStreamTrack = stream;
          //获取设备
          this.deviceList = await this.getDevice() || [];
          let video = this.$refs['video'];

          video.pause();
          video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
          if ("srcObject" in video) {
            video.srcObject = stream
          } else {
            video.src = window.URL && window.URL.createObjectURL(stream) || stream
          };
          video.play();
          video.onplay = () => {
            toast.clear();
            this.isCameraOpen = true;
            resolve({ code: `ok` });
          };
        } catch (error) {
          toast.clear();
          console.error(error);
          resolve({ errMsg: error })
        }
      })
    },
    startMediaRecorder() {
      return new Promise(async resolve => {
        if (typeof MediaRecorder === "function") {
          this.isFarArr = []; //记录远近
          this.isOpenMouthArr = []; //张嘴
          this.isWinkArr = []; //眨眼
          this.isShakingHisHeadArr = []; //摇头
          this.inProgress = false;
          const toast = this.$toast.loading({
            duration: 0, // 持续展示 toast
            forbidClick: true,
            message: '准备录制',
          });

          this.mediaRecorder = new MediaRecorder(this.mediaStreamTrack, {
            audioBitsPerSecond: 0, //音频码率
            videoBitsPerSecond: 1000000 * 20, //视频码率 (数值越大视频越清晰)
            // mimeType: 'video/webm;codecs=h264' //视频编码格式
          });
          this.mediaRecorder.start();
          // this.mediaRecorder.resume();
          this.mediaRecorder.ondataavailable = e => {
            this.blob = new Blob([e.data], {
              'type': e.currentTarget.mimeType
            });
          }
          this.mediaRecorder.onerror = e => {
            this.inProgress = false;
            console.error(e)
            toast.clear();
            resolve({ errMsg: e });
          }
          this.mediaRecorder.onstart = e => {
            this.inProgress = true;
            console.log('开始', e);
            toast.clear();
            this.$toast.loading(`开始录制`);
            resolve({ code: `ok` });
          }
          this.mediaRecorder.onresume = e => {
            this.inProgress = true;
            console.log('恢复', e);
            toast.clear();
            resolve({ code: `ok` });
          }
          this.mediaRecorder.onstop = e => {
            this.inProgress = false;
            const saveFile = this.$toast.loading({
              duration: 0, // 持续展示 toast
              forbidClick: true,
              message: '保存视频中',
            });
            //video.duration *Math.random() console.log(video.duration)

            console.log('结束', e);

            const url = window.URL && window.URL.createObjectURL(this.blob);
            this.url = url
            //const video = this.$refs.videoRef;
            // video.removeEventListener('canplay',listener)
            // video.addEventListener('canplay',listener)

            // async function listener (){
            //   while (video.duration === Infinity) {
            //     await new Promise(r => setTimeout(r, 200));
            //     video.currentTime = 10000000 * Math.random();
            //   }
            //
            //
            //
            //   //console.log(video.duration)
            //
            //
            // }

            // this.$nextTick(() =>{
            //   console.log(video.duration)
            // })

            //const randomTime = Math.floor(Math.random() * video.duration); // 随机获取视频中的时间点
            //console.log(randomTime)
            //video.currentTime = randomTime; // 设置视频的时间点
            // video.currentTime = randomTimerandomTime; // 设置视频的时间点
            // const photoCanvas = this.$refs.photoCanvas;
            // const ctx = photoCanvas.getContext('2d');
            // ctx.drawImage(video, 0, 0, photoCanvas.width, photoCanvas.height); // 绘制随机时间点的视频截图到画布上
            // const imageUrl = photoCanvas.toDataURL("image/jpeg");
            //
            // const link = document.createElement("a");
            // link.href = imageUrl;
            // link.download = "frame.jpg";
            // link.click();

            // requestAnimationFrame(()=>{
            //   const imageData = photoCanvas.toDataURL("image/jpeg");
            //   const data = atob(imageData.split(",")[1]);
            //   const buffer = new Uint8Array(data.length);
            //   for (let i = 0; i < data.length; i++) {
            //     buffer[i] = data.charCodeAt(i);
            //   }
            //
            //   // 创建并下载图片文件
            //   const blob = new Blob([buffer], { type: "image/jpeg" });
            //   const link = document.createElement("a");
            //   link.href = URL.createObjectURL(blob);
            //   link.download = "frame.jpg";
            //   document.body.appendChild(link);
            //   link.click();
            //   document.body.removeChild(link);
            // })



            // this.$dialog.confirm({
            //   title: '录制完成',
            //   message: `
            //
            //                 `
            // })
            //     .then(() => {
            //       this.$toast.loading(`上传成功！`);
            //     })
            saveFile.clear();
          }

        } else {
          this.$dialog.alert({
            title: '失败',
            message: `录制失败：浏览器不支持new MediaRecorder方法`,
            theme: 'round-button',
          }).then(() => {
            // location.replace(`${location.pathname}?s=${new Date().getTime()}`)
          });
        }
      })
    },
    async StopMediaRecorder() {
      this.inProgress = false;
      this.isCameraOpen = false;
      const toast = this.$toast.loading({
        duration: 0, // 持续展示 toast
        forbidClick: true,
        message: '已完成！保存视频中',
      });
      await this.delay(5); //所有动作结束以后 延迟五秒关闭录制。
      this.mediaStreamTrack.getVideoTracks().forEach(track => {
        track.stop();
      })
      this.mediaRecorder && this.mediaRecorder.stop();
      toast.clear();
    },
    //镜像切换
    triggerToggleFlipHorizontal() {
      this.flipHorizontal = !this.flipHorizontal;
      var video = this.$refs['video'];
      if (this.flipHorizontal) {
        video.style.transform = 'scale(-1, 1)';
      } else {
        video.style.transform = 'scale(1, 1)';
      };
      this.createDetector();
    },
    //随机生成动作
    generateAction() {
      this.$refs.actionSwipe.swipeTo(0);
      this.currentRate = 0;
      this.currentAction = [this.actionList[Math.floor(Math.random() * this.actionList.length)]].map(e => {
        e.complete = false;
        e.time = 0;
        return e
      }).sort(_ => Math.random() > 0.5 ? -1 : 1);
      //.sort(_ => Math.random() > 0.5 ? -1 : 1)
      console.log("ok");
      console.log(this.currentAction);

    },
    //显示当前动作
    showCurrentAction() {
      let name = '';
      const array = this.currentAction;
      for (let index = 0; index < array.length; index++) {
        const element = array[index];
        if (element.complete === false) {
          name = element.name;
          break;
        }
      }
      return name;
    },
    //触发动作
    triggerAction(actionValue) {
      if (this.isCameraOpen && this.inProgress) {
        let index = this.currentAction.findIndex(e => !e.complete);
        let findObj = this.currentAction.find(e => !e.complete) || {};

        let deffTime = new Date().getTime() - this.nextactionTime;
        //两个动作间隔3s
        if (findObj.value === actionValue && deffTime >= 3000) {
          this.nextactionTime = new Date().getTime();
          findObj.complete = true;
          this.$set(this.currentAction, index, findObj);
          const num = (this.currentAction.filter(e => e.complete)).length;
          this.currentRate = this.GetPercent(num, this.currentAction.length);
          this.$refs.actionSwipe.next();
        };
        let isComplete = this.currentAction.every(e => e.complete === true);
        //console.log(currentAction);
        if (isComplete) {
          console.log("complete");
          this.StopMediaRecorder();
        }
      }
    },
    //创建识别模型
    async createDetector() {
      return new Promise(async resolve => {
        this.generateAction(); //生成模型
        const toast = this.$toast.loading({
          duration: 0, // 持续展示 toast
          forbidClick: true,
          message: '加载模型中（首次加载需要1-2分钟）',
        });
        this.ModelLoading = true;
        try {
          if (!this.isObjEmpty(this.detector)) {
            this.detector.dispose();
          };
          if (!this.isObjEmpty(this.rafId)) {
            window.cancelAnimationFrame(this.rafId);
            this.rafId = null;
          };

          // const model = await faceLandmarksDetection.load(
          //     faceLandmarksDetection.SupportedModels.MediaPipeFaceMesh,
          //     {
          //       maxFaces: 1,
          //       detectorModelUrl:'src/model/blazeface.json',
          //       // 用于指定自定义 iris 模型 url 或tf.io.IOHandler对象的可选参数
          //       irisModelUrl: 'src/model/iris.json',
          //       // 用于指定自定义 facemesh 模型 url 或tf.io.IOHandler对象的可选参数
          //       modelUrl: 'src/model/facemesh.json'
          //     }
          // )
          const model = faceLandmarksDetection.SupportedModels.MediaPipeFaceMesh;
          const detectorConfig = {
            maxFaces: 1, //检测到的最大面部数量
            refineLandmarks: true, //可以完善眼睛和嘴唇周围的地标坐标，并在虹膜周围输出其他地标
            runtime: 'mediapipe',
            solutionPath: 'https://unpkg.com/@mediapipe/face_mesh', //WASM二进制文件和模型文件所在的路径
          };
          this.detector = await faceLandmarksDetection.createDetector(model, detectorConfig);
          toast.clear();
          this.rafId = window.requestAnimationFrame(this.renderPrediction);
          resolve({ code: `ok` });
        } catch (error) {
          toast.clear();
          this.ModelLoading = false;
          // this.$dialog.alert({
          //     title: '失败',
          //     message: `创建识别模型失败-${error}`,
          //     theme: 'round-button',
          // }).then(() => {
          //     location.replace(`${location.pathname}?s=${new Date().getTime()}`)
          // });
          this.detector = null;
          console.log(error);
          resolve({ errMsg: error });
        }
      })
    },

    //预测
    async renderPrediction() {
      var video = this.$refs['video'];
      var canvas = this.$refs['canvas'];
      var context = canvas.getContext('2d');
      if (this.detector && this.isCameraOpen) {
        try {
          context.clearRect(0, 0, canvas.width, canvas.height);
          const Faces = await this.detector.estimateFaces(video, {
            flipHorizontal: this.flipHorizontal, //镜像
          });

          this.ModelLoading = false;
          if (Faces.length > 0) {
            this.faceNullFrequency = 0;
            this.drawResults(Faces, context);
          } else {
            this.faceNullFrequency++;
            //连续5帧没有检测到人脸提示
            if (this.faceNullFrequency >= 5) {
              this.$toast.loading(`没有检测到人脸`);
            }
          }
        } catch (error) {
          this.createDetector();
          this.ModelLoading = false;
          this.$toast.loading(`预测-${error}`);
          console.log(error);
          context.clearRect(0, 0, canvas.width, canvas.height);
        }
        this.rafId = window.requestAnimationFrame(this.renderPrediction);
      } else {
        context.clearRect(0, 0, canvas.width, canvas.height);
        this.rafId = window.requestAnimationFrame(this.renderPrediction);
      }
    },
    //绘制
    drawResults(faces, ctx) {
      faces.forEach(faceItem => {
        ctx.fillStyle = '#1af117';
        (faceItem.keypoints || []).forEach((element, index) => {
          /* arc */
          ctx.beginPath();
          ctx.arc(element.x, element.y, 1, 0, 2 * Math.PI);
          ctx.fill();
          /* arc */
        });
        const faceProportion = this.GetPercent(faceItem.box.width * faceItem.box.height, this.width * this.height);
        this.$refs['faceProportion'].innerHTML = `10-20之间,当前距离:<b>${Math.round(faceProportion)}</b>`;
        //this.faceDistance = Math.round(faceProportion);
        //console.log(this.faceDistance);
        if( Math.round(faceProportion)<=20 && Math.round(faceProportion) >=10){
          this.faceDistanceisOK=true;
        }
        else{
          this.faceDistanceisOK=false;
        }
        //console.log(this.faceDistanceisOK);
        if (faceProportion <= 10) {
          this.$toast.loading(`距离太远`);
          return;
        };
        if (faceProportion >= 20) {
          this.$toast.loading(`距离太近`);
          return;
        };
        if (this.isCameraOpen && this.inProgress) {
          //靠近&远离
          this.isFarAndNear(faceItem);
          // console.log("1");
          //张嘴
          this.isOpenMouth(faceItem, ctx);
          //  console.log("2");
          //眨眼
          this.isWink(faceItem, ctx);
          // console.log("3");
          //摇头
          this.isShakingHisHead(faceItem, ctx);
          //console.log("4");
        }
      });
    },

    //靠近&远离
    isFarAndNear(face) {
      const proportion = this.GetPercent(face.box.width * face.box.height, this.width * this.height);
      this.isFarArr.push(proportion);
      //计算4帧的动态变化
      if (this.isFarArr.length > 4) {
        this.isFarArr.shift();
        if (this.Increment(this.isFarArr) || this.Decrease(this.isFarArr)) {
          const first = this.isFarArr[0];
          const last = this.isFarArr[this.isFarArr.length - 1];
          const diff = this.GetPercent(first - last, first + last);
          if (diff <= -5) {
            console.log("靠近了");
            this.triggerAction(1);
          };
          if (diff >= 5) {
            console.log("远离了");
            this.triggerAction(0);
          };
        }
      };
    },
    //张嘴
    isOpenMouth(face, ctx) {

      const featureIndex1 = [0, 17];
      const featureLocation1 = [];

      const featureIndex2 = [10, 152];
      const featureLocation2 = [];

      (face.keypoints || []).forEach((element, index) => {
        if (featureIndex1.includes(index)) {
          featureLocation1.push([element.x, element.y])
        }
        if (featureIndex2.includes(index)) {
          featureLocation2.push([element.x, element.y])
        }
      });

      // 10,152占0,17的比例
      const proportion = this.GetPercent(this.getDistance(
          featureLocation1[0][0],
          featureLocation1[0][1],
          featureLocation1[1][0],
          featureLocation1[1][1],
      ), this.getDistance(
          featureLocation2[0][0],
          featureLocation2[0][1],
          featureLocation2[1][0],
          featureLocation2[1][1],
      ));
      this.isOpenMouthArr.push(proportion);

      //计算2帧的动态变化
      if (this.isOpenMouthArr.length > 2) {
        this.isOpenMouthArr.shift();
        if (this.Increment(this.isOpenMouthArr)) {
          const first = this.isOpenMouthArr[0];
          const last = this.isOpenMouthArr[this.isOpenMouthArr.length - 1];
          const diff = this.GetPercent(first - last, first + last);
          if (diff <= -5) {
            // this.log(`【动作】张嘴`, `info`);
            this.triggerAction(2);
          };
        }
      }

    },

    isWink(face, ctx) {//眨眼判断

      const leftEye = [159, 144];
      const leftEyeLocation = [];
      const rightEye = [385, 374];
      const rightEyeLocation = [];

      (face.keypoints || []).forEach((element, index) => {
        if (leftEye.includes(index)) {
          leftEyeLocation.push([element.x, element.y]);
        }
        if (rightEye.includes(index)) {
          rightEyeLocation.push([element.x, element.y]);
        }
      });

      let leftProportion = this.getDistance(
          leftEyeLocation[0][0],
          leftEyeLocation[0][1],
          leftEyeLocation[1][0],
          leftEyeLocation[1][1],
      );
      let rightProportion = this.getDistance(
          rightEyeLocation[0][0],
          rightEyeLocation[0][1],
          rightEyeLocation[1][0],
          rightEyeLocation[1][1],
      );

      if (leftProportion <= 5 || rightProportion <= 5) {
        this.isWinkArr.push([leftProportion, rightProportion]);
        //连续4帧一次
        if (this.isWinkArr.length >= 4) {
          // this.log(`【动作】眨眼`, `info`);
          this.triggerAction(3);
          this.isWinkArr = [];
        }
      } else {
        this.isWinkArr = [];
      }
    },
    //isShakingHisHead
    isShakingHisHead(face, ctx) {
      const leftFace = [195, 93];
      const leftFaceLocation = [];
      const rightFace = [195, 323];
      const rightFaceLocation = [];

      (face.keypoints || []).forEach((element, index) => {
        if (leftFace.includes(index)) {
          leftFaceLocation.push([element.x, element.y]);
        }
        if (rightFace.includes(index)) {
          if (rightFaceLocation.length === 0) {
            ctx.moveTo(element.x, element.y)
          } else {
            ctx.lineTo(element.x, element.y)
          }
          rightFaceLocation.push([element.x, element.y]);

        }
      });
      let leftProportion = this.getDistance(
          leftFaceLocation[0][0],
          leftFaceLocation[0][1],
          leftFaceLocation[1][0],
          leftFaceLocation[1][1],
      );
      let rightProportion = this.getDistance(
          rightFaceLocation[0][0],
          rightFaceLocation[0][1],
          rightFaceLocation[1][0],
          rightFaceLocation[1][1],
      );

      const diff = this.GetPercent(leftProportion - rightProportion, leftProportion + rightProportion);
      this.isShakingHisHeadArr.push(diff); //左 -40 右 40

      //计算4帧的动态变化
      if (this.isShakingHisHeadArr.length > 4) {
        this.isShakingHisHeadArr.shift();
        const isL = this.isShakingHisHeadArr.every(e => e >= -60);
        const isR = this.isShakingHisHeadArr.every(e => e <= 60);
        if (isL) {
          // this.log(`【动作】向左转`, `info`);
          this.triggerAction(4);
        }
        if (isR) {
          // this.log(`【动作】向右转`, `info`);
          this.triggerAction(5);
        }
      };
      // console.log(diff);
    },
    actionSelect(value) {
      const { deviceId } = value;
      this.actionShow = false;
      if (!this.isObjEmpty(deviceId) && this.deviceId != deviceId) {
        this.deviceId = deviceId;
        window.localStorage.setItem(`deviceId`, deviceId);
        this.openUserMedia();
      }

    },
    //获取设备信息
    getDevice() {
      return new Promise(async resolve => {
        const toast = this.$toast.loading({
          duration: 0, // 持续展示 toast
          forbidClick: true,
          message: '获取设备中',
        });
        try {
          const devicesList = await navigator.mediaDevices.enumerateDevices();
          const arr = [];
          (devicesList || []).forEach(e => {
            e.name = e.label || e.deviceId;
            if (e.kind === "videoinput" && e.deviceId && !e.name.includes('麦克风')) {
              e.color = e.deviceId == this.deviceId ? '#1989fa' : '#323233';
              arr.push(e)
            }
          });
          toast.clear();
          console.log(arr);
          resolve(arr);
        } catch (error) {
          toast.clear();
          console.log(error);
          resolve([]);
        };
      })
    },
    // 一堆兼容代码
    compatible() {
      window.URL = (window.URL || window.webkitURL || window.mozURL || window.msURL);
      if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {};
      }
      if (navigator.mediaDevices.getUserMedia === undefined) {
        navigator.mediaDevices.getUserMedia = (constraints) => {
          var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
          if (!getUserMedia) {
            return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
          }
          return new Promise((resolve, reject) => {
            getUserMedia.call(navigator, constraints, resolve, reject);
          });
        }
      }
    },
    //递增
    Increment(array) {
      let is = true;
      for (let i = 0; i < array.length - 1; i++) {
        var n1 = array[i];
        var n2 = array[i + 1];
        if (n1 > n2) {
          is = false;
          break;
        }
      }
      return array.length > 1 ? is : false
    },
    //递减
    Decrease(array = []) {
      let is = true;
      for (let i = 0; i < array.length - 1; i++) {
        var n1 = array[i];
        var n2 = array[i + 1];
        if (n1 < n2) {
          is = false;
          break;
        }
      }
      return array.length > 1 ? is : false
    },

    //距离
    getDistance(x1, y1, x2, y2) {
      return Math.sqrt((x2 -= x1) * x2 + (y2 -= y1) * y2);
    },
    /**
     * @ 占比计算
     * @ num 当前数
     * @ total 总数
     */
    GetPercent(num, total) {
      num = parseFloat(num);
      total = parseFloat(total);
      if (isNaN(num) || isNaN(total)) {
        return "-";
      }
      return total <= 0 ? 0 : (Math.round(num / total * 10000) / 100.00);
    },
    /**
     * 毫秒数的可读格式
     */
    formatDuration(time) {
      let h = parseInt(time / 60 / 60 % 24)
      h = h < 10 ? '0' + h : h
      let m = parseInt(time / 60 % 60)
      m = m < 10 ? '0' + m : m
      let s = parseInt(time % 60)
      s = s < 10 ? '0' + s : s
      // 作为返回值返回
      return h === "00" ? [m, s].join(':') : [h, m, s].join(':')
    },
    //延迟
    delay(m = 1) {
      return new Promise(res => {
        setTimeout(() => {
          res(true);
        }, m * 1000);
      })
    }
  }
}
</script>
<style scoped>
@import '../style/main.css';
</style>