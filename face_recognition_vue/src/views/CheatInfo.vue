<template>
  <div>
    <div style="margin-top: 2rem">
      <h1>人脸欺骗信息</h1>
    </div>
    <div>
      <el-table
          :data="CheatInfoData"
          style="width: 100%"
          :key="CheatInfoData.id"
      >
        <el-table-column
            fixed
            prop="ip"
            label="ip"
            width="180">
        </el-table-column>
        <el-table-column
            prop="authenticity"
            label="识别结果"
            width="120">
        </el-table-column>
        <el-table-column
            prop="confidence"
            label="置信度"
            width="120">
        </el-table-column>
        <el-table-column
            prop="time"
            label="时间"
            width="180">
        </el-table-column>
      </el-table>
      <div style="position: absolute; bottom: 15rem;left:50rem">
        <div class="block">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[8]"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="totalSize">
          </el-pagination>
        </div>
      </div>

    </div>
  </div>

</template>

<script>
export default {
  name: "CheatInfo",
  data:function (){
    return{
      CheatInfoData:[
        {
          id:'',
          authenticity:'',
          time: '',
          confidence:'',
          ip:''
        }
      ],
      //初始页
      currentPage: 1,
      pageSize: 8,
      totalSize: 10
    }
  },
  mounted() {
    this.getRecordsPage();

  },
  methods: {
    getRecordsPage(){
      this.$axios.post("http://101.43.93.152:6006/records/getRecordsPage",{pageSize:this.pageSize,currentPage:this.currentPage}).then(
          res => {
            if (res.data.code == 0){
              this.totalSize = res.data.data.total
              let CheatInfoData = res.data.data.list;
              for (let i = 0; i<CheatInfoData.length;i++){
                if (CheatInfoData[i].authenticity === 1){
                  CheatInfoData[i].authenticity = '通过';
                }else {
                  CheatInfoData[i].authenticity = '未通过';
                }
              }
              this.CheatInfoData = CheatInfoData;
            }
          },
          err => {
            console.log(err)
          }
      )
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.currentPage = val
      this.getRecordsPage();
    }
  }
}
</script>

<style scoped>

</style>