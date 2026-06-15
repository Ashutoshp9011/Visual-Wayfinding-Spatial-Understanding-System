package com.ashutosh.core_navigation.export

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.ashutosh.core_navigation.graph.NavigationGraph
import com.google.gson.Gson

class MapExporter(private val graph: NavigationGraph) {

    fun toJson(): String = Gson().toJson(graph)

    fun toSvg(width: Int, height: Int): String = buildString {
        append("""<svg viewBox="0 0 $width $height" xmlns="http://www.w3.org/2000/svg">""")
        graph.edges.forEach { e ->
            val a = graph.nodes[e.from]!!; val b = graph.nodes[e.to]!!
            append("""<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="#555" stroke-width="2"/>""")
        }
        graph.rooms.values.forEach { r ->
            append("""<rect x="${r.boundingBox.left}" y="${r.boundingBox.top}" width="${r.boundingBox.width()}" height="${r.boundingBox.height()}" fill="#e8f4fd" stroke="#333"/>""")
            append("""<text x="${r.boundingBox.centerX()}" y="${r.boundingBox.centerY()}" text-anchor="middle" font-size="12">${r.number}</text>""")
        }
        append("</svg>")
    }

    fun toPng(context: Context, width: Int, height: Int): Bitmap {
        val bmp = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        val canvas = Canvas(bmp)
        val paint = Paint(Paint.ANTI_ALIAS_FLAG)

        // Draw edges
        paint.color = Color.GRAY
        paint.strokeWidth = 2f
        graph.edges.forEach { e ->
            val a = graph.nodes[e.from]!!
            val b = graph.nodes[e.to]!!
            canvas.drawLine(a.x, a.y, b.x, b.y, paint)
        }

        // Draw rooms
        graph.rooms.values.forEach { r ->
            paint.style = Paint.Style.FILL
            paint.color = Color.parseColor("#e8f4fd")
            canvas.drawRect(r.boundingBox, paint)
            paint.style = Paint.Style.STROKE
            paint.color = Color.DKGRAY
            canvas.drawRect(r.boundingBox, paint)

            // Draw room labels
            paint.style = Paint.Style.FILL
            paint.color = Color.BLACK
            paint.textSize = 12f
            paint.textAlign = Paint.Align.CENTER
            canvas.drawText(r.number, r.boundingBox.centerX(), r.boundingBox.centerY(), paint)
        }
        return bmp
    }
}
