<template>
  <div>
    <div class="title">
      <h1>人脸识别导航</h1>
      <hr style="border: black solid 2px"/>
    </div>
    <div class="face">
      <div class="faceRecognition" @click="faceRecognition">
        <div class="picture1">
          <img src="../static/人脸识别.png">
        </div>
        <div class="font_style">
          前端使用tensorflow捕捉关键点，并传输人脸照片到后端识别并返回结果
        </div>
      </div>
      <div class="faceInfoGet" @click="faceInfoGet">
        <div class="picture1">
          <img src="../static/人脸录入.png">
        </div>
        <div class="font_style">
          前端使用tensorflow捕捉关键点，并传输人脸照片到后端录入
        </div>
      </div>
      <div class="faceInfo" @click="faceInfo">
        <div class="picture1">
          <img src="../static/识别记录.png">
        </div>
        <div class="font_style">
          人脸识别信息查看，当用户被识别时会在此留下记录，可以查看有哪些用户使用了该系统
        </div>
      </div>
      <div class="cheatInfo" @click="cheatInfo">
        <div class="picture1">
          <img src="../static/安全信息.png">
        </div>
        <div class="font_style">
          查看有什么时间，什么ip企图用人脸欺骗攻击系统
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Navigation",
  data:function (){
    return{

    }
  },
  methods: {
    faceRecognition(){
      this.$router.push("/faceRecognition")
    },
    faceInfoGet(){
      this.$router.push("/faceInfoGet")
    },
    faceInfo(){
      this.$router.push("/faceInfo")
    },
    cheatInfo(){
      this.$router.push("/cheatInfo")
    }
  },
  // mounted() {
  //   this.$axios.get("/api/help/getip.php").then(
  //       res => {
  //         console.log(res)
  //       }
  //   ).catch(
  //       err =>{
  //         console.log(err)
  //       }
  //   )
  // }
}
</script>

<style scoped>
.title {
  margin-top: 1rem;
  text-align: center;
  font-size: 25px;
}
.face {
  width: 90rem;
  height: 40rem;
  margin-top: 2rem;
  margin-left: -20rem;
}
.faceRecognition {
  display: inline-block;
  width: 20rem;
  height: 30rem;
  border: 8px dotted #99CC00;
  border-radius: 2rem;
  padding-top: 10%;
  margin: 0 1.5rem 0 1rem ;
}
.faceInfoGet {
  display: inline-block;
  width: 20rem;
  height: 30rem;
  border: 8px ridge #CC9999;
  border-radius: 2rem;
  padding-top: 10%;
}
.faceInfo {
  display: inline-block;
  width: 20rem;
  height: 30rem;
  border: 8px outset #FF6600;
  border-radius: 2rem;
  padding-top: 10%;
  margin: 0 1.5rem 0 1rem ;
}
.cheatInfo {
  display: inline-block;
  width: 20rem;
  height: 30rem;
  border: 10px double #FF9999;
  border-radius: 2rem;
  padding-top: 10%;
}
.picture1 {
  margin-top: -8rem;
  height: 80%;
}
.picture1 img {
  width: 100%;
  height: 100%;
}
.font_style {
  margin-top: 4rem;
  padding: 2rem;
  font-weight: bolder;
  font-size: 18px;
  font-family: STZhongsong;
}



</style>