package com.example.in_solve

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import com.example.in_solve.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

     binding = ActivityMainBinding.inflate(layoutInflater)
     setContentView(binding.root)

        // Example of a call to a native method
        binding.entrance.text = stringFromJNI()
    }
    /**
      * A native method that is implemented by the 'in_solve' native library,
      * which is packaged with this application.
      */
     external fun stringFromJNI(): String

     companion object {
         // Used to load the 'in_solve' library on application startup.
         init {
             System.loadLibrary("in_solve")
         }
     }
}