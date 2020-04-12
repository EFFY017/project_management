<template>
  <VmTable title="员工信息管理"
           type="edit"
           :columns="dataColumns"
           :data="dataTable"
           v-on:add-ok="add"
           v-on:edit-ok="edit"
           v-on:delete-ok="deletefn"
           class="vm-margin">
  </VmTable>
</template>

<script>
import VmTable from '../back/vm-table'
export default {
  name: 'BackWorker',
  components: {
    VmTable
  },
  methods: {
    add: function (data) {
      this.dataTable.unshift(data)
    },
    edit: function (data) {
      this.dataTable.forEach(function (elem) {
        if (elem.id === data.id) {
          for (let i in data) {
            elem[i] = data[i]
          }
        }
      })
    },
    deletefn: function (data) {
      for (let i = 0; i < this.dataTable.length; i++) {
        for (let j = 0; j < data.length; j++) {
          if (this.dataTable[i].id === data[j].id) {
            this.dataTable.splice(i, 1)
          }
        }
      }
    }
  },
  data () {
    return {
      dataColumns: [
        {
          id: '20156541',
          title: '用户名',
          key: 'username'
        },
        {
          id: '20156542',
          title: '密码',
          key: 'password'
        },
        {
          id: '20156543',
          title: '姓名',
          key: 'name'
        },
        {
          id: '20156544',
          title: '职位',
          key: 'career'
        },
        {
          id: '20156545',
          title: '部门',
          key: 'department'
        }
      ],
      dataTable: [
        {
          username: 'admin',
          password: '123456',
          name: '张三',
          career: '算法工程师',
          department: '开发'

        },
        {
          username: '1',
          password: '123456',
          name: '李四',
          career: '开发工程师',
          department: '开发'
        },
        {
          username: '2',
          password: '123456',
          name: '王二',
          career: '测试工程师',
          department: '开发'
        }
      ]
    }
  }
}
</script>
