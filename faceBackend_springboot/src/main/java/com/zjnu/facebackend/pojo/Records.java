package com.zjnu.facebackend.pojo;


import lombok.Data;

import java.io.Serializable;

import java.util.Date;


/**
* 
* @TableName records
*/

@Data
public class Records implements Serializable {

    private Integer id;

    /**
    * 1代表通过，0代表未通过
    */
    private Integer authenticity;

    private Date time;

    private Integer confidence;

    private String ip;


}
